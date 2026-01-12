# Rebuild VPS tanpa Login ke Panel

Panduan ini memberikan instruksi untuk melakukan rebuild VPS pada berbagai distribusi Linux tanpa perlu login ke panel. Anda dapat mengunduh dan menjalankan skrip yang disediakan untuk memulai proses.

## Distribusi dan Versi yang Didukung

#Rebuild:
```
debian      9|10|11|12
centos      9|10
ubuntu      16.04|18.04|20.04|22.04|24.04|24.10 [--minimal]
almalinux   8|9
windows     10|11|server
```

## Langkah-langkah

1. Download skrip `reinstall.sh`.

   ```bash
   curl -O https://raw.githubusercontent.com/Nizwara/reinstall/main/reinstall.sh
   ```
2. OR
   ```bash
   bash <(curl https://raw.githubusercontent.com/Nizwara/reinstall/main/reinstall.sh) debian 10
   ```
   ```
   bash <(curl https://raw.githubusercontent.com/Nizwara/reinstall/main/reinstall.sh) debian 11
   ```
   ```
   bash <(curl https://raw.githubusercontent.com/Nizwara/reinstall/main/reinstall.sh) ubuntu 20.04
   ```
3. Jalankan skrip dengan memilih distribusi dan versi sistem operasi yang diinginkan.

### Contoh Perintah

#### Ubuntu

Instal Ubuntu versi 24.10, 24.04, 22.04, 20.04, 18.04, atau 16.04:

```bash
bash reinstall.sh ubuntu 24.10
```

```bash
bash reinstall.sh ubuntu 24.04
```

```bash
bash reinstall.sh ubuntu 22.04
```

```bash
bash reinstall.sh ubuntu 20.04
```

```bash
bash reinstall.sh ubuntu 18.04
```

```bash
bash reinstall.sh ubuntu 16.04
```

Untuk instalasi minimal Ubuntu:

```bash
bash reinstall.sh ubuntu 24.10 --minimal
```

#### Debian

Instal Debian versi 12 (Bookworm), 11 (Bullseye), 10 (Buster), atau 9 (Stretch):

```bash
bash reinstall.sh debian 12
```

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

Instal CentOS versi 10 atau 9:

```bash
bash reinstall.sh centos 10
```

```bash
bash reinstall.sh centos 9
```

#### AlmaLinux

Instal AlmaLinux versi 9 atau 8:

```bash
bash reinstall.sh almalinux 9
```

```bash
bash reinstall.sh almalinux 8
```

#### Windows

Instal Windows (akan mencari ISO otomatis dari massgrave.dev):

**Supported Versions:**
- **Windows 10:** Consumer (Home/Pro/Edu), Business (Pro/Enterprise), LTSC (2015, 2016, 2019, 2021)
- **Windows 11:** Consumer (Home/Pro/Edu), Business (Pro/Enterprise), LTSC (2024)
- **Windows Server:**
  - 2025 (Standard, Datacenter)
  - 2022 (Standard, Datacenter)
  - 2019 (Standard, Datacenter)
  - 2016 (Standard, Datacenter)
  - 2012 R2 (Standard, Datacenter)
  - 2008 R2 (Standard, Datacenter, Enterprise, Web)
  - 2008 (Standard, Datacenter, Enterprise, Web)

**Format:**
```bash
bash reinstall.sh windows --image-name="windows [version] [edition]" --lang=[language]
```

**Contoh (Examples):**

Windows 10 Pro:
```bash
bash reinstall.sh windows --image-name="windows 10 pro" --lang=en-us
```

Windows 11 Pro:
```bash
bash reinstall.sh windows --image-name="windows 11 pro" --lang=en-us
```

Windows 10 LTSC 2021:
```bash
bash reinstall.sh windows --image-name="windows 10 enterprise ltsc 2021" --lang=en-us
```

Windows Server 2025 Standard:
```bash
bash reinstall.sh windows --image-name="windows server 2025 standard" --lang=en-us
```

Windows Server 2022 Datacenter:
```bash
bash reinstall.sh windows --image-name="windows server 2022 datacenter" --lang=en-us
```

Windows Server 2012 R2 Datacenter:
```bash
bash reinstall.sh windows --image-name="windows server 2012 r2 datacenter" --lang=en-us
```

Jika Anda menjalankan dari Windows, gunakan `reinstall.bat` (Run as Administrator):
```cmd
reinstall.bat windows --image-name="windows 11 pro"
```
