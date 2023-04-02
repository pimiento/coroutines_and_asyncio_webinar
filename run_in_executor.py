#!/usr/bin/env python3
import asyncio
from requests import get
from contextlib import asynccontextmanager

@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    yield await loop.run_in_executor(
        None, get, url)
async def main():
    async with web_page(
            "https://ya.ru") as data:
        print(data.content.decode("utf-8"))
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
