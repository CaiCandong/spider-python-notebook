import asyncio
from typing import List
import requests 
import time 
"""
小bug,ssl模块找不到
conda找错了openssl的地址
conda在Anaconda\DLLs目录下寻找openssl的dll文件
但实际上需要的dll在Anaconda3\library\bin目录下。
因此只需要将这两个文件复制到 Anaconda\DLLs下即可。
https://github.com/conda/conda/issues/8273
"""
# requests 为同步的http请求,无法做到异步请求
async def request():
    # url  = "https://www.httpbin.org/delay/5"
    # status = requests.get(url )
    await asyncio.sleep(5)
    # return status 

async def main():
    start = time.time()
    tasks:List[asyncio.Task] = [asyncio.create_task(request()) for _ in range(2)]
    print(tasks)
    await asyncio.gather(*tasks)

    for task in tasks :
        print(task.result)
    end = time.time()

    print("cost time",end-start)
asyncio.run(main())
