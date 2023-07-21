#!/usr/bin/env python

import datetime

N = 100_000_000
start_time = datetime.datetime.now()

i, j = 0, 0

while i < N:
    i += 1
    j += i

print(i)
print(f"Time required {(datetime.datetime.now() - start_time).total_seconds()}s.")
