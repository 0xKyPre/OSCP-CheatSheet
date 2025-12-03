# Windows Privilege Escalation – OSCP Markdown
## Step 1 - Basic System Enumeration
```
whoami
whoami /priv
systeminfo
hostname
```

## Step 2 - Users & Groups
```
net user
net localgroup administrators
```

## Step 3 - Services & Processes
```
tasklist /v
sc query
wmic service list brief
```

## Step 4 - Files & Permission Issues
- Unquoted Service Paths
- Weak File/Service Permissions
- Startup folder permissions

**AlwaysInstallElevated Check**
```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

## Step 5 - Autologon Check
```
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

## Step 6 - Network Enumeration
```
ipconfig /all
netstat -ano
route print
arp -a
```

## Step 7 - Useful Tools
- winPEAS
- Seatbelt
- SharpUp