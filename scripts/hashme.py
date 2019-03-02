#! /usr/local/bin/python3

import sys, subprocess, hashlib, base64

try:
    site = sys.argv[1]
except IndexError:
    print("Usage: please enter some text (quoted if spaces)")
    sys.exit()

if len(sys.argv) > 1:
   try:
       n = int(sys.argv[2])
   except:
       n = 20

kf = "/home/pi/.ssh/id_rsa.pub"
#kf = "/Users/telliott_admin/.ssh/id_rsa.pub"

with open(kf) as file:
    key_data = file.read().strip().split()[1]
    s = key_data + site

m = hashlib.sha256()
m.update(s.encode('utf8'))
d = m.digest()
b = base64.b64encode(d)
# convert to string
b = b.decode('utf-8')

D = {'+':'', '/':''}
tt = str.maketrans(D)
b = b.translate(tt)

print(b[:n])

