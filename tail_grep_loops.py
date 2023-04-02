#!/usr/bin/env python3
def follow(filepath, grepper):
    with open(filepath, "r") as fd:
        # "сикнемся" в конец файла
        fd.seek(0, 2)
        while True:
            line = fd.readline()
            if not line:
                # небольшая пауза
                time.sleep(0.1)
                continue
            grepper(line)
import time

def grep(pattern):
    pattern = pattern.lower()
    def match(line):
        if pattern in line.lower():
            print(line)
    return match

follow("/tmp/t.txt", grep("python"))
