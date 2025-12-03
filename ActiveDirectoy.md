# Active Directory – OSCP Markdown
## Step 1 - Basic Domain Enumeration
```
whoami /groups
nltest /dsgetdc:<domain>
```

## Step 2 - User, Group & Share Enumeration
```
net user /domain
net group /domain
net view \\host /all
```

## Step 3 - Kerberos Basics
- SPN Enumeration
- Kerberos Tickets (`klist`)

**Common Kerberos Misconfigurations**
- Kerberoasting
- AS-REP Roasting
- Delegation misconfigurations

## Step 4 - GPO & LDAP Enumeration
```
gpresult /r
gpupdate /force
```

## Step 5 - BloodHound
- SharpHound data collection
- Analyze:
    + Weak ACLs
    + Abusable group memberships
    + Delegation issues