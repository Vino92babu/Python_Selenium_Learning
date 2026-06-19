import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://leaftaps.com/opentaps/control/main")
driver.maximize_window()
page_tittle = driver.title
page_url = driver.current_url
print(page_tittle)
print(page_url)
time.sleep(2)
