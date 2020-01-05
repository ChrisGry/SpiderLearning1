from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://morvanzhou.github.io/static/scraping/table.html")
soup = BeautifulSoup(html,"html.parser")

#找出所有图片链接
# .*表示非空白符号可以出现0或无数次，？表示前面的正则表达式匹配0或1次
img_links = soup.find_all('img',{'src':re.compile(r".*?\.jpg")})
for link in img_links:
    print(link["src"])

#找出非图片链接
print("not picture")
img_links1 = soup.find_all('a',{'href':re.compile(r"https://morvan.*")})
for link in img_links1:
    print(link['href'])