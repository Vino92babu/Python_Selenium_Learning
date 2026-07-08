from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

# from Selenium.webelements import Countries

driver=webdriver.Chrome()
'''driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#Check box
#Static check box
driver.find_element(By.XPATH,'//input[@id="checkBoxOption2"]').click()
# Dynamic check box- when it changes its position
chkbx = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
print(len(chkbx))
for checkbox in chkbx:
    if checkbox.get_attribute("value")=="option3":
        checkbox.click()
        assert checkbox.is_selected()

        print(checkbox.get_attribute("value"))
        break
'''
# Radio Button
# Static Radio button
# driver.get("https://www.sreenidhirajakrishnan.com/practice?utm_source=sp_auto_dm&utm_referrer=sp_auto_dm&fbclid=PAT01DUASvkt1leHRuA2FlbQIxMABzcnRjBmFwcF9pZA81NjcwNjczNDMzNTI0MjcAAaecrzPgG4Ywp8o5SYBeclsS7CPfX2WGpd8T0HWsnqHvGe8jgUb91LcAIF1nzg_aem_hPrp5rPeLzIUNLz60JBw9g")
# driver.maximize_window()
# radio_option=driver.find_elements(By.XPATH,"//select[@id='standard-select']")
# print(len(radio_option))
# for option in radio_option:
#     if option.get_attribute("value") == "Green":
#         option.click()
#         print(option.get_attribute("value"))
#         break

# dropdown = Select(driver.find_element(By.ID, "standard-select"))
#
# dropdown.select_by_visible_text("Red")
# time.sleep(2)
# dropdown.select_by_value("blue")
# message = driver.find_element(By.ID, "standard-select").text

# driver.get("https://practice.expandtesting.com/dropdown")
# driver.maximize_window()
# countries = driver.find_elements(By.XPATH,'//select[@id="country"]/option')
# print(len(countries))
# print(countries.get_attribute("value"))
# for Country in countries:
#     if Country.text == "India":
#         Country.click()
#         break


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# Select(driver.find_element(By.XPATH,'//select[@id="dropdown-class-example"]')).select_by_value('option2')
# driver.find_element(By.XPATH,'//select[@id="dropdown-class-example"]').click()
dropdowns = driver.find_elements(By.XPATH,'//select[@id="dropdown-class-example"]/option')
print(len(dropdowns))
for dropdown in dropdowns:
    if dropdown.get_attribute("value") == "option2":
        dropdown.click()
        assert driver.find_element(By.XPATH,'//select[@id="dropdown-class-example"]').get_attribute('value') == 'option2'
        break







time.sleep(5)