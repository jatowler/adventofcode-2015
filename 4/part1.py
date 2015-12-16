#!/usr/bin/env python

import hashlib


def hash_with_salt(string, salt):
    return hashlib.md5(str(string) + str(salt)).hexdigest()

with open('input', 'r') as f:
    # Strip the trailing newline
    data = f.read()[:-1]

cur_salt = 0
while True:
    cur_hash = hash_with_salt(data, cur_salt)

    if cur_hash.startswith('00000'):
        print '{} with salt {} produces hash {}'.format(data,
                                                        cur_salt,
                                                        cur_hash)
        break

    cur_salt = cur_salt + 1

    if cur_salt % 10000 == 0:
        print 'Processing salt {}'.format(cur_salt)
