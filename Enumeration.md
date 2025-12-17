# Enumeration – OSCP Markdown
## Step 1 - Host Discovery
```
nmap -sn 10.0.0.0/24
arp-scan 10.0.0.0/24
```

## Step 2 - Port Scanning
```
nmap -sV -sC -Pn -p- <target>
nmap -p- --min-rate 5000 -T4 -oN fastscan.txt <TARGET_IP>
```
- `-p-`: all 65535 Ports (without only top 1000 Ports)
- `-sV`: service and version detection
- `sC`: default NSE Scripts
- `-Pn`: nmap assumes that the host is always online
- `T4`: fast scan
- `-oN`: output normal -> writes output to file
- `--min-rate <RATE>`: min package sent per second

**Goal:** Identify 1–2 high-value services to attack first (Web, SMB, SSH, FTP).


**OSCP - 2 STEP Parallel to bruteforce/wpscan/hydra/dirbuster/gobuster**
```
nmap -p- --min-rate 5000 -T4 <IP>
nmap -sC -sV -p <open_ports> <IP>
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

If SMB open -> enum `anonymously` first before creds brute-force.

## Step 5 - Web Content Discovery
```
gobuster dir -u http://target -w wordlist.txt
ffuf -u http://target/FUZZ -w wordlist.txt
```

For faster enumeration and less noise use http-response-code check
```
ffuf -u http://target/FUZZ -w wordlist.txt -mc 200,301,302
```

**FOR ALL ENUMERATION DONE SCREENSHOTS AND/OR COPY OF IP, PORT, SERVICES, VERSIONS!**