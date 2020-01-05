import requests

def getHTMLText503(url):
    try:
        #处理503错误
        kv = {'user-agent':'Mozilla/5.0'}

        r = requests.get(url,timeout = 30,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        #显示status_code，确实为200
        print("status: "+str(r.status_code))

        return r.text
    except:
        return "出现异常: "+str(r.status_code)

if __name__ == "__main__":
    url = "https://www.amazon.cn/dp/B07NZLSZZ4/"
    print(getHTMLText503(url)[:3000])