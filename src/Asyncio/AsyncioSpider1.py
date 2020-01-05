import time
import requests
import asyncio

#正常情况下爬取网页
URL = 'https://morvanzhou.github.io/'

#爬取两遍
def normal():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)

t1 = time.time()
normal()
print('Normal Total time: ',time.time()-t1)

#Asyncio下爬取网页
import aiohttp

async def job(session):
    response = await session.get(URL)
    return str(response.url)

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(job(session)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        #这些tasks执行后的返回对象，需要用result()得到原始函数的返回值
        all_results = [r.result() for r in finished]
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print('Asyncio Total time: ',time.time()-t1)
