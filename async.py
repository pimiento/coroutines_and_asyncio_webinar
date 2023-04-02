#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=8)

def func(x, y):
    import time
    time.sleep(1)
    return x + y
def result_handler(fut):
    result = fut.result()
    print('Got:', result)
def run():
    fut = pool.submit(func, 2, 3)
    fut.add_done_callback(
        result_handler
    )
run()
print("DONE")
