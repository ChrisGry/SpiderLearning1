import requests
import os

def getHTMLImage(url,root):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        #保存图片
        path = root + url.split('/')[-1]
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            with open(path,'wb') as f:
                f.write(r.content) #r.content返回r的内容的二进制
                f.close()

        return "图片保存成功！"

    except:
        return "出现异常"+str(r.status_code)

if __name__ == "__main__":
    path = "D:/pycharmWorkspace/WebCrawler/pic/"
    url = "http://image.ngchina.com.cn/2019/0802/20190802012904270.jpg"
    print(getHTMLImage(url,path))