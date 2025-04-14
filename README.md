```markdown
# Rebuild VPS tanpa Login ke Panel

Panduan ini memberikan instruksi untuk melakukan rebuild VPS pada berbagai distribusi Linux tanpa perlu login ke panel. Anda dapat mengunduh dan menjalankan skrip yang disediakan untuk memulai proses.

## Langkah-langkah

1. Download skrip `reinstall.sh`.

   ```bash
   curl -O https://raw.githubusercontent.com/bin456789/reinstall/main/reinstall.sh
   ```

2. Jalankan skrip dengan memilih distribusi dan versi sistem operasi yang diinginkan.

### Contoh Perintah

#### Ubuntu

Instal Ubuntu versi 22.04, 20.04, atau 18.04:

```bash
bash reinstall.sh ubuntu 22.04
```

```bash
bash reinstall.sh ubuntu 20.04
```

```bash
bash reinstall.sh ubuntu 18.04
```

#### Debian

Instal Debian versi 11 (Bullseye), 10 (Buster), atau 9 (Stretch):

```bash
bash reinstall.sh debian 11
```

```bash
bash reinstall.sh debian 10
```

```bash
bash reinstall.sh debian 9
```

#### CentOS

Instal CentOS versi 8 atau 7:

```bash
bash reinstall.sh centos 8
```

```bash
bash reinstall.sh centos 7
```

### Catatan

- Pastikan untuk mengganti versi dengan yang sesuai kebutuhan Anda.
- Skrip ini akan melakukan instalasi ulang sistem operasi, jadi pastikan untuk membackup data penting sebelum melanjutkan.
- Gunakan perintah ini dengan kehati-hatian dan pahami risiko yang terkait dengan proses reinstall sistem operasi.

Dengan mengikuti panduan ini, Anda dapat dengan mudah mengubah dan mengelola distribusi Linux pada VPS Anda sesuai kebutuhan.
```

Silakan salin teks di atas dan tempelkan ke dalam `README.md` Anda di GitHub. Formating Markdown akan diterapkan sehingga kontennya terlihat rapi dan jelas ketika dilihat di GitHub.
