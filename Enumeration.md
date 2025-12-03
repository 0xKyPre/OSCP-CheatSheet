# Enumeration – OSCP Markdown
## Step 1 - Host Discovery
```
nmap -sn 10.0.0.0/24
arp-scan 10.0.0.0/24
```

## Step 2 - Port Scanning
```
nmap -sV -sC -Pn -p- <target>
```

## Step 3 - Banner Grabbing
```
nc -nv <target> <port>
curl -I http://<target>
```

## Step 4 - Service Enumeration
```
SMB: smbclient -L \\host -N

FTP: ftp <host>

SSH: ssh -v <host>
```

## Step 5 - Web Content Discovery
```
gobuster dir -u http://target -w wordlist.txt
ffuf -u http://target/FUZZ -w wordlist.txt
```