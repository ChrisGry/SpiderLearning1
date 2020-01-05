import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常: "+r.status_code

if __name__ == "__main__":
    url = "https://item.jd.com/2967929.html"
    print(getHTMLText(url)[:1000]) #只返回前1000个字符