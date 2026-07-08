import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

'''input text'''
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@id="username"]').send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("Learning@830$3mK2")

'''DropDown - Static'''

Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_value("teach")
Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_index(0)
Select(driver.find_element(By.XPATH,'//select[@class="form-control"]')).select_by_visible_text("Consultant")

'''DropDown - Auto_Suggestive '''
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()



time.sleep(2)