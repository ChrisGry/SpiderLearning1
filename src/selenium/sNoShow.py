from selenium import webdriver
#如何在后台点击不需要显示浏览器
from selenium.webdriver.chrome.options import Options
co = Options()
co.add_argument('--headless')

#加入参数
driver = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe',options=co)
#其他代码不变
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"大家说").click()
driver.find_element_by_link_text("About").click()

html = driver.page_source
print(html[:200])
driver.get_screenshot_as_file('../../pic/sc2.png')
driver.close()