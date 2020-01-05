from selenium import webdriver

driver = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe')
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"大家说").click()
driver.find_element_by_link_text("About").click()

html = driver.page_source
driver.get_screenshot_as_file('../../pic/sc.png')
driver.close()

