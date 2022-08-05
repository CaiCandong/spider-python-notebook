import json
from typing import Dict, List
import aiohttp 
import logging 
import asyncio
# ********************mongodb*************#
from motor.motor_asyncio import AsyncIOMotorClient
MONGO_CONNECTION_STIRNG ="mongodb://localhost:27017"
MONGO_DB_NAME = "books"
MONGO_COLLECTION_NAME = "books"
clinet = AsyncIOMotorClient(MONGO_CONNECTION_STIRNG)
db = clinet[MONGO_DB_NAME]
collection= db[MONGO_COLLECTION_NAME]

async def save_data(data):
    logging.info("saving data %s",data)
    if data:
        return await collection.update_one({
            'id':data.get('id')
        },{
            '$set':data
        },upsert= True)

# SSL报错：
# https://github.com/conda/conda/issues/8273

logging.basicConfig(level=logging.INFO,
        format ='%(asctime)s-%(levelname)s: %(message)s')


# 最大并发量(信号量)
CONCURRENCY = 3
PAGE_NUMBER = 100
PAGE_SIZE=18 
# session :aiohttp.ClientSession  = None 
session  = None 
semaphore = asyncio.Semaphore(CONCURRENCY)
api = "https://spa5.scrape.center/api/book"

async def scrape_api(url):
    async with semaphore:
        try:
            async with session.get(url) as response :
                return await response.json()
        except aiohttp.ClientError:
            logging.error("error")

async def scrape_index(page):
    offset  = (page-1)*PAGE_SIZE
    url = f"https://spa5.scrape.center/api/book/?limit=18&offset={offset}"
    return await  scrape_api(url)

async def scrape_detail(id):
    url = f"https://spa5.scrape.center/api/book/{id}"
    data =  await  scrape_api(url)
    await save_data(data)
    return data 

async def main():
    global session 
    session = aiohttp.ClientSession()
    # 获取索引页信息
    # scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1,PAGE_NUMBER+1)]
    scrape_index_tasks = [asyncio.create_task(scrape_index(page)) for page in range(1,PAGE_NUMBER+1)]
    results:List[Dict]= await asyncio.gather(*scrape_index_tasks)
    # logging.info("results %s",json.dumps(results,ensure_ascii=False,indent=2))
    # 根据索引页信息获取详情页链接
    ids = []
    for index_data in results:
        if not index_data:
            continue 
        for item in index_data.get("results"):
            ids.append(item.get('id'))
    
    scrape_detail_tasks = [asyncio.create_task(scrape_detail(id )) for id  in ids]
    details = await asyncio.gather(*scrape_detail_tasks)
    # for detail in details :
    # with open("data.json",'w',encoding='utf8') as f : 
    #     json.dump(details,f,ensure_ascii=False,indent=2)
    # with open("data.json",'w',encoding='utf8') as f :
    #     json.dump(results,f,ensure_ascii=False,indent=2)
    #     # f.write(json.dumps(results,ensure_ascii=False,indent=2))
    session.close()

if __name__ =="__main__":
    # 使用run 方法和ensure_future会有冲突,不在同一个事件循环
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())

        
