import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常: "+str(r.status_code)

#使用get的params参数
def getHTMLTextBaidu():
    try:
        url = "http://www.baidu.com/s"
        kv = {'wd':'吴彦祖'}
        r = requests.get(url,timeout=30,params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常: "+str(r.status_code)

if __name__ == "__main__":
    url = "http://www.baidu.com/s?wd=吴彦祖"
    print(getHTMLTextBaidu())
