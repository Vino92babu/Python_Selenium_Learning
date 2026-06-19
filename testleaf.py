import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://leaftaps.com/opentaps/control/main")
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("democsr")

driver.find_element(By.ID,"password").send_keys("crmsfa")
driver.find_element(By.CLASS_NAME,"decorativeSubmit").click()
time.sleep(2)