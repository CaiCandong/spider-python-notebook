import asyncio

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(3,"等待3s"))
    task2 = asyncio.create_task(say_after(1,"等待2s"))
    await task2

asyncio.run(main())