# Rebuild VPS tanpa Login ke Panel

Panduan ini memberikan instruksi untuk melakukan rebuild VPS pada berbagai distribusi Linux tanpa perlu login ke panel. Anda dapat mengunduh dan menjalankan skrip yang disediakan untuk memulai proses.

## Distribusi dan Versi yang Didukung

#Rebuild:
```
debian      9|10|11|12
centos      9|10
ubuntu      16.04|18.04|20.04|22.04|24.04|24.10 [--minimal]
almalinux   8|9
```

## Langkah-langkah

1. Download skrip `reinstall.sh`.

   ```bash
   curl -O https://raw.githubusercontent.com/Nizwara/reinstall/main/reinstall.sh
   ```

2. Jalankan skrip dengan memilih distribusi dan versi sistem operasi yang diinginkan.

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
