# Rebuild VPS without Panel Login

This guide provides instructions for rebuilding a VPS with various Linux distributions without needing to log in to a control panel. You can download and run the provided script to start the process.

## Supported Distributions and Versions

#Rebuild:
```
debian      9|10|11|12
centos      9|10
ubuntu      16.04|18.04|20.04|22.04|24.04|24.10 [--minimal]
almalinux   8|9
windows     10|11|server
```

## Steps

1. Download the `reinstall.sh` script.

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
3. Run the script by selecting the desired operating system distribution and version.

### Command Examples

#### Ubuntu

Install Ubuntu version 24.10, 24.04, 22.04, 20.04, 18.04, or 16.04:

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

For Ubuntu minimal installation:

```bash
bash reinstall.sh ubuntu 24.10 --minimal
```

#### Debian

Install Debian version 12 (Bookworm), 11 (Bullseye), 10 (Buster), or 9 (Stretch):

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

Install CentOS version 10 or 9:

```bash
bash reinstall.sh centos 10
```

```bash
bash reinstall.sh centos 9
```

#### AlmaLinux

Install AlmaLinux version 9 or 8:

```bash
bash reinstall.sh almalinux 9
```

```bash
bash reinstall.sh almalinux 8
```

#### Windows

Install Windows (will automatically search for ISO from massgrave.dev):

**Supported Versions:**
- **Windows 10:** Consumer (Home/Pro/Edu), Business (Pro/Enterprise), LTSC (2015, 2016, 2019, 2021)
- **Windows 11:** Consumer (Home/Pro/Edu), Business (Pro/Enterprise), LTSC (2024)
- **Windows Server:**
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

**Examples:**

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

Windows Server 2022 Datacenter:
```bash
bash reinstall.sh windows --image-name="windows server 2022 datacenter" --lang=en-us
```

Windows Server 2012 R2 Datacenter:
```bash
bash reinstall.sh windows --image-name="windows server 2012 r2 datacenter" --lang=en-us
```

If you are running from Windows, use `reinstall.bat` (Run as Administrator):
```cmd
reinstall.bat windows --image-name="windows 11 pro"
```
