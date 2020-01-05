import multiprocessing as mp
import time
from urllib.request import urlopen,urljoin
from bs4 import BeautifulSoup
import re #正则表达式

base_url = 'https://morvanzhou.github.io/'

#爬取网页
def crawl(url):
    response = urlopen(url)
    time.sleep(0.1)
    return response.read().decode()

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

#使用单进程
unseen = set([base_url,])
seen = set()
#计数，计时
count, t1 = 1,time.time()

while len(unseen) > 0:
    #莫烦python网站只可以访问20个页面
    if len(seen)>20:
        break;

    print('/n Crawling...')
    htmls = [crawl(url) for url in unseen]
    print('/n Parsing...')
    results = [parse(html) for html in htmls]
    #print(results)
    print('/n Analysing...')
    seen.update(unseen)
    unseen.clear()

    for title,page_urls,url in results:
        print(count,': ',title,' ',url)
        count = count+1
        unseen.update(page_urls-seen)

    #print(unseen)

print('Total time: %.lf s' % (time.time()-t1))
