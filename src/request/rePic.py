#下载图片

IMAGE_URL = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'

#使用urllib库的retreive方法
from urllib.request import urlretrieve
urlretrieve(IMAGE_URL,'../../pic/img1.png')

#使用requests库
import requests
r = requests.get(IMAGE_URL)
#python的文件写入操作
with open('../../pic/img2.png','wb') as f:
    f.write(r.content)

#下载大文件时，如何chunk by chunk的下载
r1 = requests.get(IMAGE_URL,stream = True)
with open('../../pic/img3.png','wb') as f:
    for chunk in r1.iter_content(chunk_size=32): #chunk大小为32字节
        f.write(chunk)
