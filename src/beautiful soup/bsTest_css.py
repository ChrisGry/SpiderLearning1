from bs4 import BeautifulSoup
from urllib.request import urlopen

#打开网页
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html")

#放入BS中
soup = BeautifulSoup(html,"html.parser")

#针对<li>，只选出class='month'的
month = soup.find_all('li',{'class':'month'})

for m in month:
    #m是html标签
    #get_text()只显示文字内容，而不是整个html标签
    print(m.get_text())

#针对<ul>，只选出class='jan'的；注意这里是find函数而不是find_all
jan = soup.find('ul',{'class':'jan'})
print('jan:',jan)

day = jan.find_all('li')

for d in day:
    #m是html标签
    #get_text()只显示文字内容，而不是整个html标签
    print(d.get_text())

#find函数和find_all函数的区别；find只返回一个html的对象，而find_all会返回一个数组，每个元素是一个html的没有嵌套的小标签
jan1 = soup.find_all('ul',{'class':'jan'})

print("jan1:",jan1)

for j in jan1:
    print(j.get_text())