#!/usr/bin/env python3
import crypt
import getpass
import os

passwd = getpass.getpass()
hashed = crypt.crypt(passwd, crypt.mksalt(crypt.METHOD_SHA512))

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pass'), 'w') as fp:
    fp.write(hashed)

