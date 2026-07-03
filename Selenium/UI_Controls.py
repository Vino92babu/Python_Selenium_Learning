from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#Check box
#Static check box
# driver.find_element(By.XPATH,'//input[@id="checkBoxOption2"]').click()
# Dynamic check box- when it changes its position
chkbx = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
print(len(chkbx))
for checkbox in chkbx:
    if checkbox.get_attribute("value")=="option3":
        checkbox.click()
        assert checkbox.is_selected()

        print(checkbox.get_attribute("value"))
        break

# Radio Button
# Static Radio button
driver.find_element()






time.sleep(2)