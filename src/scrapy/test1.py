import scrapy

#继承Spider类，创建一个子类
class GrySpider(scrapy.Spider):
    #爬取莫烦python教学的全网站内容
    name = 'Gry' #定义name属性
    start_urls =['https://morvanzhou.github.io/',]

    def parse(self, response):

        #python的yield关键字，函数‘对象’返回yield的内容后，会暂停当前函数‘对象’的执行；这里是为了实现异步
        yield{ #提取当前网页的标题和网址，存储为json格式的文件
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace("",""),
            'url': response.url,
        }

        #找到当前网页中全部的网址
        urls = response.css('a::attr(href)').re(r'^/.+?/$')

        #对新的每一个网址重复用parse去解析
        for url in urls:
            yield response.follow(url,callback = self.parse)



