from bs4 import BeautifulSoup
import requests

url = 'http://www.ngchina.com.cn/animals/'

html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

img_ul = soup.find_all('ul',{'class':'img_list'})
print(len(img_ul))#有两个ul组件，一个里面有3副图

#下载图片
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url1 = img['src']
        r1 = requests.get(url1,stream=True)
        imgName = url1.split('/')[-1]
        with open('../../pic/%s' % imgName, 'wb') as f:
            for chunk in r1.iter_content(chunk_size=128):
                f.write(chunk)
        print('Save %s' % imgName)

