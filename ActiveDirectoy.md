# Active Directory – OSCP Markdown

## AD - Attacks
- AS-SEP Roasting
- Kerberoasting
- DCSync Attacks
- Windows PrivEsc
- Mimikatz/credentials extraction
- Pass-The-Hash
- Pivoting
- Lateral Movement Basics
- Bloodhound

## Active Directoy Introduction and Enumeration

### Important Enumeration and Lateral Movement Tools
#### crackmapexec
Extremly useful when you want to test credentials to known windows services such as **smb**, **winrm** or **rdp**.
```
crackmapexec {param_1} {param_2} -u USERNAME -p PASSWORD

crackmapexec smb IP -u USERNAME -H NTLM-HASH
crackmapexec rdp IP_1 IP_2 -u USERNAME -p PASSWORD
```
- `param_1`: protocoll we want to test
- `param_2`: list of ips, single ip or file with list of ips
- `-u`: username
- `-p`: password
- `-H`: ntlm-hash in case we dont have the password

#### evil-winrm
When you have access to the winrm protocol then you can use evil-winrm to get a functional shell in which you can upload and download files even when connected via a socks5 proxy with proxychain connection.
```
evil-winrm -i IP -u USERNAME -p PASSWORD 
```

#### sharp-hound
Tool used to collect all possible informations about a given domain. 

#### bloud-hound
Pretty good visualisation for the data collected by sharp-hound.

#### chisel
See in the [Pivoting and Tunneling - Chisel](./PivotingTunneling.md#step-3c---chisel) dokumentation

## Attacking Active Directory Authentification

### Install impacket
first make new python environment:
```
python3 -m venv venv
```
then start the environment
```
. venv/bin/activate
```
then install impacket
```
pip3 install impacket
```

### Tools
When compromising an active directory you need to be able to understand and use these 5 tools:

#### Mimikatz
Most important tool for active directory exploiting. When downloading the basic mimikatz you will have problems with antivirus. BUT **OSCP** is **NOT** about **ANTIVIRUS ENVASION** so you dont need to worry. **OSEP** THOUGH IS ABOUT ENVADING ANTIVIRUS!!!!! 

```
./mimikatz64.exe "privilege::debug" "sekurlsa::logonPasswords full" "exit"
```

#### Kerberoasting

#### AS-SEP roasting

#### DCSync Attacks

#### Capture NET-NTLMv2 hashes with responder 

#### Relay NET-NTLMv2 hashes with ntlmrelayx 

## Lateral Movement in Active Directory

### Pass the Hash

### Overpass the Hash

### Pass the Ticket

### Golden Ticket