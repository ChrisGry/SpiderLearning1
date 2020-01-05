from bs4 import BeautifulSoup as bs
import requests

url = "https://python123.io/ws/demo.html"
r = requests.get(url,timeout=30)
demo = r.text

soup = bs(demo,"html.parser")
print(r.text)
print("-----------------------------------------")
print(soup.prettify())