#!/usr/bin/env python3
# async downloader
async def rng(n):
    for i in range(n):
        yield i

async def foo(n):
    async for i in rng(n):
        print(i)
# sync scheduler
def task(n):
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(foo(n))

# register sync task in the sceduler
task(5)
