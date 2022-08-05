# 使用ensure_future方法
# 手动创建task
import asyncio
import requests 
async def request():
    url  = "http://www.baidu.com"
    status = requests.get(url )
    return status 

def callback(task ):
    print("Status",task.result())

coroutine = request()
# Future类的实例都表示可能完成或者尚未完成的延迟计算
# Wrap a coroutine or an awaitable in a future.
# If the argument is a Future, it is returned directly
# 变量：类型 =>显式增强代码提示
task :asyncio.Task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print(task)
print("After calling loop")