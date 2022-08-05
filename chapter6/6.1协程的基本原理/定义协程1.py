# 显式事件循环loop
# 自动创建task
import asyncio
async def execute(x):
    print("Number",x)

coroutine = execute(1)
print("croutine:",coroutine)
print("After calling execute")

# 获取事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print("After calling loop")