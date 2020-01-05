import requests

"""
r = requests.get("http://www.baidu.com")
if r.status_code==200:
    r.encoding='utf-8'
    print(r.status_code)
    print(r.text)
    print(type(r))
    print(r.headers)
"""

"""
r = requests.get("http://www.baidu.com")
if r.status_code==200:
    r.encoding = r.apparent_encoding
    print(r.text)
"""

#网络爬虫通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常: "+str(r.status_code)

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
