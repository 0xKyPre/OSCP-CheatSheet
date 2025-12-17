# Cryptography and Dictionary

## RSA -> Passphrase
Imagine you have this rsa-private Key:
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,E32C44CDC29375458A02E94F94B280EA

JCPsentybd...
...g1yIGR81cR+W
-----END RSA PRIVATE KEY-----
```

```sh
# safe the key
nano id_rsa
chmod 600 id_rsa

# generate hash
ssh2john id_rsa > rsa.hash

# crack it
john --wordlist=/usr/share/wordlists/rockyou.txt rsa.hash

# result
john --show rsa.hash

# decrypt
openssl rsa -in id_rsa -out id_rsa_decrypted
```

## MD5
```
hashcat -m 0 -a 0 hash.txt wordlist.txt
```

## Dictionary
sometimes when dictionaries are really big its better to delete all duplicates before bruteforce
```
sort word.dic | uniq > word_clean.txt
```