import requests
import webbrowser

#使用百度搜索‘莫烦python’;百度搜索，通过get方法‘wd’参数提交关键词
param = {'wd':'莫烦python'}
r = requests.get("http://www.baidu.com/s",params=param)
print(r.url)
webbrowser.open(r.url)

#使用post像表单form那样提交信息
postUrl = 'http://pythonscraping.com/pages/files/processing.php'
data = {'firstname':'Ryan','lastname':'Guan'}
r1 = requests.post(postUrl,data=data)
print(r1.text)

#使用Post上传图片，注意表单组件的名字
postUrl2 = 'http://pythonscraping.com/pages/files/processing2.php'
file2 = {'uploadFile':open('../../pic/20190802010628808.jpg','rb')}
r2 = requests.post(postUrl2,files = file2)
print(r2.text)

#使用Post登录
postUrl3 = 'http://pythonscraping.com/pages/cookies/welcome.php'
data3 = {'username':'gry','password':'password'}
r3 = requests.post(postUrl3,data = data3)
print(r3.text)
#此处显示“未成功登录”，但应该是登录成功，welcome.php配置错误，必须接收cookies信息才能产生正确的页面
#如何实现连续访问：传递上一个页面cookies的信息；注意上下为同一个网址
print(r3.cookies.get_dict())
r4 = requests.get(postUrl3,cookies = r3.cookies)
print(r4.text)
#此处可以登录成功

#建立一个session来管理cookies
session = requests.Session()
data4 = {'username':'g','password':'password'}
r5 = session.post(postUrl3,data = data4)
print(r5.cookies.get_dict())
#session已经包含了cookies
r6 = session.get(postUrl3)
print(r6.text)




