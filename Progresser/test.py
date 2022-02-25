from base64 import b64encode as encode
from random import choice
from string import ascii_letters as letters
st = "upload_progress_"
st_len = len(st)
for i in range(300):
    if i - 2> st_len and (i - 2) % 9 == 0:
        to_enc =  st + "".join(choice(letters) for _ in range(st_len, i - 2))
        if b"=" not in encode(to_enc.encode()) and b"=" not in encode(encode(to_enc.encode())) and b"=" not in encode(encode(encode(to_enc.encode()))):
            print(f"[+] {to_enc}", i, i - 2)
