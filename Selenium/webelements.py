import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://www.rahulshettyacademy.com/angularpractice/")
# driver.find_element(By.NAME,"name").send_keys("Vinoth")
# driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,'input[placeholder="Password"]').send_keys("Admin123")
# driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()

# Dropdown-Static


# dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# dropdown.select_by_index(1)
# dropdown.select_by_visible_text('Male')
# driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
# driver.find_element(By.CSS_SELECTOR,'input[value="Submit"]').click()
# message=driver.find_element(By.CLASS_NAME,"alert").text
# print(message)
# time.sleep(5)

# Dropdown - Auto-suggestion
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
Countries=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
print(len(Countries))
for Country in Countries:
    if Country.text == "India":
        Country.click()
        break
# else:
#     print("Their is no word you declared in this country!Kindly Check")
# This one wont work. bcos .text method captured the only text when url is loaded. not the automated
# dp = driver.find_element(By.ID,"autosuggest").text
# print(dp)
#Instead use java script dom ,use get attribute("Value)
dp = driver.find_element(By.ID,"autosuggest").get_attribute("value")
print(dp)
assert dp == "India"
# or
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"