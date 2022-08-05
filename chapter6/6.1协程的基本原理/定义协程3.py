# 使用ensure_future方法
# 手动创建task
import asyncio
async def execute(x):
    print("Number",x)
    return x 
coroutine =execute(1)
print("croutine:",coroutine)
print("After calling execute")

task = asyncio.ensure_future(coroutine)
print(task)
# 获取事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print(task)
print("After calling loop")