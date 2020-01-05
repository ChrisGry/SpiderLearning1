import multiprocessing as mp
import time
from urllib.request import urlopen,urljoin
from bs4 import BeautifulSoup
import re #正则表达式
import aiohttp
import asyncio

#初始化参数
base_url = 'https://morvanzhou.github.io/'
unseen = set([base_url,])
seen = set()

#爬取网页
async def crawl(url,session):
    response = await session.get(url)
    html = await response.text()
    await asyncio.sleep(0.1)
    return html

#分析网页内容
def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    #提取所有网址
    urls = soup.find_all('a',{"href": re.compile('^/.+?/$')})
    #提取标题
    title = soup.find('h1').get_text().strip() #strip（）移除字符串首尾的空格和换行

    #set()创建一个无序不重复的元素集；urljoin()构建一个完整的绝对url地址
    page_urls = set([urljoin(base_url,url['href']) for url in urls] )

    #当前网页的url
    url = soup.find('meta',{'property':"og:url"})['content']
    return title, page_urls, url

async def main(loop):
    pool = mp.Pool(4)
    async with aiohttp.ClientSession() as session:
        count = 1
        while len(unseen) > 0:
            if len(seen) > 20:
                break;

            print('/n Asyncio Crawling')
            tasks = [loop.create_task(crawl(url,session)) for url in unseen]
            finished, unfinished = await asyncio.wait(tasks)
            htmls = [f.result() for f in finished]

            print('/n Multi-processing Parse')
            parse_jobs = [pool.apply_async(parse,args=(html,)) for html in htmls]
            results = [j.get() for j in parse_jobs]

            print('/n Analysing')
            seen.update(unseen)
            unseen.clear()
            for title, page_urls, url in results:
                print(count,' ',title,': ',url)
                count=count+1
                unseen.update(page_urls-seen)

if __name__ == "__main__":
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
    print('Best Total time: %.1f s' % (time.time()-t1))
