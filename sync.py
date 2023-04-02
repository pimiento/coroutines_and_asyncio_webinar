#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=8)
def func(x, y):
  import time
  time.sleep(1)
  return x + y
def run():
  fut = pool.submit(func, 2, 3)
  r = fut.result()
  print('Got:', r)
run()
print("DONE")
