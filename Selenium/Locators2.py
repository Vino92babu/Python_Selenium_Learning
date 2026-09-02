import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("123")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("123")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(2)



'''Locating with respect to elements and Attribite
 syntax: //input[@attribute = 'value'] 

 * --> tagname
 @id --> attribute

1    Locating element with known attribute. 
ex://*[@attribute = 'value']
2    Locating element with known tagname & Atrribute
ex: //input[@maxlength="15"]
3    Location Element with known visible text[Exact Match]
ex:  //*[text()='Name:']
4    Location Element with known visible text[partial Match]
ex:  //*[contains(text(),'Name:')]
5    Locating elements with Multiple Attributes
ex://*[@type="text"][@id="name"][@class="form-control"]
6    Locating elements when starting visible text is known
ex: //*[starts-with(text(),'abc']

Locating Element relative to known elements:
1    Locating a parent element
ex: //*[@id="textarea"]/parent::div
2    Locating a child element
//*[@class="form-group"]/child::input
3    Locating following element
//*[@id='123']/following::div
//*[@id='123']/following::div[3]-->to find ecact element
4    Locating preceding element
//*[@id='123']/preceding::div[3]
5    Locating following slibling
//*[@id='123']/following-sibling::div[3]
6 Locating preceeding slibling
//*[@id='123']/preceding-sibling::div[3]
Syntax: 
//*[@atributename= 'value]



Automation Testing Practice

//*[@class="oxd-input-group oxd-input-field-bottom-space"]/parent::div/parent::form/child::div[3]/following-sibling::div/child::p

'''



