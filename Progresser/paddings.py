import base64
import string

good_chars = string.digits + string.ascii_uppercase + string.ascii_lowercase + '+/'
sl = []
for i in range(len(good_chars)):
	for j in range(len(good_chars)):
		try:
			str = 'upload_progress_'
			str = str + good_chars[i] + good_chars[j]
			print(str)
			s = base64.b64decode(str)
			s = base64.b64decode(s)
			s = base64.b64decode(s)
			if s.decode() == '':
				sl.append(str)
		except:
			pass
print(sl)

# Generating paddings
# method by @rive_n
# works like this:
# every seq is % by 3 and % by 6 and 9
# so we could generate seq for this amount of bytes

from base64 import b64encode as encode
from random import choice
from string import ascii_letters as letters
st = "upload_progress_t_"
st_len = len(st)
for i in range(300):
    if i % 8 == 0 and i * 8 % 6 != 0:
        if i - 2> st_len:
            to_enc =  st + "".join(choice(letters) for _ in range(st_len, i - 2))
            if b"=" not in encode(to_enc.encode()) and b"=" not in encode(encode(to_enc.encode())) and b"=" not in encode(encode(encode(to_enc.encode()))):
                print(f"[+] {to_enc}")
