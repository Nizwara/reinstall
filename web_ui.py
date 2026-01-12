import http.server
import socketserver
import json
import subprocess
import sys
import os

PORT = 8000

class ReinstallHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/run':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            distro = data.get('distro')
            version = data.get('version')
            password = data.get('password')
            port = data.get('port')
            image_name = data.get('image_name')
            iso = data.get('iso')
            rdp_port = data.get('rdp_port')
            img = data.get('img')

            cmd = ['bash', 'reinstall.sh', distro]

            if version:
                cmd.append(version)

            if password:
                cmd.extend(['--password', password])

            if port:
                cmd.extend(['--ssh-port', port])

            if distro == 'windows':
                if image_name:
                    cmd.extend(['--image-name', image_name])
                if iso:
                    cmd.extend(['--iso', iso])
                if rdp_port:
                    cmd.extend(['--rdp-port', rdp_port])

            if distro == 'dd' and img:
                cmd.extend(['--img', img])

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Transfer-Encoding', 'chunked')
            self.end_headers()

            try:
                # Start the process
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1
                )

                # Stream output
                for line in process.stdout:
                    chunk_bytes = line.encode('utf-8')
                    self.wfile.write(f"{len(chunk_bytes):X}\r\n".encode('utf-8'))
                    self.wfile.write(chunk_bytes)
                    self.wfile.write(b"\r\n")
                    self.wfile.flush()

                process.wait()
                end_msg = f"Exited with code {process.returncode}"
                chunk_bytes = end_msg.encode('utf-8')
                self.wfile.write(f"{len(chunk_bytes):X}\r\n".encode('utf-8'))
                self.wfile.write(chunk_bytes)
                self.wfile.write(b"\r\n")
                self.wfile.write(b"0\r\n\r\n")

            except Exception as e:
                err_msg = f"Error: {str(e)}"
                chunk_bytes = err_msg.encode('utf-8')
                self.wfile.write(f"{len(chunk_bytes):X}\r\n".encode('utf-8'))
                self.wfile.write(chunk_bytes)
                self.wfile.write(b"\r\n")
                self.wfile.write(b"0\r\n\r\n")
        else:
            self.send_error(404)

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    with ReusableTCPServer(("", PORT), ReinstallHandler) as httpd:
        print(f"Serving at port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
