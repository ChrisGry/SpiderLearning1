from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.baidu.com").read().decode("utf-8")
#print(html)

soup = BeautifulSoup(html,"html.parser") #features表示解析的形式

#需要提取<title></title>之间的内容
print(soup.title)
#需要提取<p></p>之间的内容
print(soup.p)

#提取超链接
all_href = soup.find_all('a')
for l in all_href:
    print(l['href']) #soup中网页元素标签变为类似字典的结构