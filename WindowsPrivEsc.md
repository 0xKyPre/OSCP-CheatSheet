# Windows Privilege Escalation – OSCP Markdown
## Step 1 - Basic System Enumeration
```
whoami
whoami /groups
whoami /priv

systeminfo
hostname
```

**If you see:**
- SeImpersonatePrivilege
- SeAssignPrimaryTokenPrivilege
**Then:**
- `JuicyPotato` / `PrintSpoofer` -> **SYSTEM**

## Step 2 - Users and Groups
```
net user
net localgroup administrators
```

## Step 3 - Services and Processes
```
tasklist /v
sc query
wmic service list brief
```
```powershell
sc query state= all
sc qc <service>
```

**Check:**
- Unquoted Service Paths
- Writable service binaries
- Writable service directories

Replace binary -> restart service -> **SYSTEM**

## Step 3.5 - Scheduled Tasks and PATH Hijacking

### Scheduled Tasks
```
schtasks /query /fo LIST /v
```

**Check:**
- Task runs as SYSTEM
- Executable or script path writable
- Runs periodically or on boot/logon

**Exploit:**
- Replace binary/script
- Wait or trigger task
-> SYSTEM

### PATH Hijacking
```
echo %PATH%
```

Check each directory:
```
icacls "C:\Program Files"
icacls "C:\Program Files (x86)"
```

**If writeable PATH directoy found:**
```
echo @echo off > evil.bat
echo powershell -c "Start-Process cmd -Verb runAs" >> evil.bat
```

## Step 4 - Stored Credentials
```
cmdkey /list
reg query HKLM /f password /t REG_SZ /s
```

Autologon:
```
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

Reuse creds -> admin / **SYSTEM**

## Step 5 - AlwaysInstallElevated
```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

If HKLM + HKCU exist:
MSI as **SYSTEM** -> full compromise

## Step 6 - Useful Tools
- winPEAS
- Seatbelt
- SharpUp

## Step 7 - Post Exploit / Network Enumeration
```
ipconfig /all
netstat -ano
route print
arp -a
```