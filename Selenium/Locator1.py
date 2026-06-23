import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Vinoth")
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Password"]').send_keys("Admin123")
driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR,'input[value="Submit"]').click()
message=driver.find_element(By.CLASS_NAME,"alert").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Babu")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(2)


