# 显式事件循环loop
# 手动创建task
import asyncio
async def execute(x):
    print("Number",x)

coroutine =execute(1)
print("croutine:",coroutine)
print("After calling execute")

# 获取事件循环
loop = asyncio.get_event_loop()

# 手动创建task
task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)
print("After calling loop")