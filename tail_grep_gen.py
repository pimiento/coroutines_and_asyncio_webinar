#!/usr/bin/env python3
import time
def grep(pattern, lines):
    pattern = pattern.lower()
    for line in lines:
        if pattern in line.lower():
            yield line
def follow(filepath):
    with open(filepath, "r") as fd:
        fd.seek(0, 2)
        while True:
            line = fd.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
for line in grep(
    "python", follow("/tmp/t.txt")
):
    print(line)
