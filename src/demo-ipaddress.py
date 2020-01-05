import requests

if __name__ == "__main__":
    url = "http://www.882667.com/ip_"
    r = requests.get(url+"114.212.83.56"+".html",timeout=30)
    try:
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("出现错误:"+str(r.status_code))
        print(r.text)