#!/usr/bin/env python3
import time

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start
def follow(filepath, target):
    with open(filepath, "r") as fd:
        fd.seek(0,2)
        while True:
            line = fd.readline()
            if not line:
                time.sleep(0.1)
                continue
            target.send(line)
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
follow("/tmp/t.txt", broadcast(
    [printer(), printer()]))
