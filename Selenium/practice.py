import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()

'''input text'''
def Login_page():
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("rahulshettyacademy")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("Learning@830$3mK2")
# Login_page()

'''DropDown - their are two types of DropDown - Static / Auto_Suggestive '''

def DropDown_Static():
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("rahulshettyacademy")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("Learning@830$3mK2")
    Select(driver.find_element(By.XPATH, '//select[@class="form-control"]')).select_by_value("teach")
    Select(driver.find_element(By.XPATH, '//select[@class="form-control"]')).select_by_index(0)
    Select(driver.find_element(By.XPATH, '//select[@class="form-control"]')).select_by_visible_text("Consultant")
# DropDown_Static()

def DrpDown_Auto_Suggestive():
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@id="autosuggest"]').send_keys("ind")
    time.sleep(2)
    Countries = driver.find_elements(By.XPATH, '//li[@class="ui-menu-item"]/a')
    print(len(Countries))
    for Country in Countries:
        if Country.text == "India":
            # print(Country.text)
            Country.click()
            break
    # print(driver.find_element(By.XPATH,'//input[@id="autosuggest"]').get_attribute("value")) == "India"
    assert driver.find_element(By.XPATH, '//input[@id="autosuggest"]').get_attribute("value") == "India"
    time.sleep(2)
# DrpDown_Auto_Suggestive()

'''Checkbox --> Static/Dynamic'''

def Checkbox_Static():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']").click()
    assert driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']").is_selected()
# Checkbox_Static()

def Checkbox_Dynamic():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox"]')
    print(len(checkboxes))
    for Checkbox in checkboxes:
        if Checkbox.get_attribute("id") == "checkBoxOption3":
            Checkbox.click()
            assert Checkbox.is_selected()
            break
    time.sleep(2)
# Checkbox_Dynamic()

'''Radio Button'''

def Radio_btn_static():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    driver.find_element(By.XPATH,'//input[@value="radio1"]').click()
    assert driver.find_element(By.XPATH,'//input[@value="radio1"]').is_selected()
# Radio_btn_static()

def Radio_btn_dynamic():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    Radio_options = driver.find_elements(By.XPATH,'//input[@name="radioButton"]')
    print(len(Radio_options))
    for Radio_btn in Radio_options:
        if Radio_btn.get_attribute('value') == "radio3":
            Radio_btn.click()
            assert driver.find_element(By.XPATH,'//input[@value="radio3"]').is_selected()
            break
# Radio_btn_dynamic()

'''is_displayed ---> use to find the element is present on the page or not'''

def isdisplayed():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    driver.find_element(By.XPATH,'//input[@id="displayed-text"]').is_displayed()
    assert driver.find_element(By.XPATH,'//input[@id="displayed-text"]').is_displayed()
    driver.find_element(By.XPATH, '//input[@id="hide-textbox"]').click()
    # assert driver.find_element(By.XPATH, '//input[@id="displayed-text"]').is_displayed()
    assert not driver.find_element(By.XPATH, '//input[@id="displayed-text"]').is_displayed()
# isdisplayed()

'''Alerts'''
Name = "Vinoth"
def alert():
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    driver.find_element(By.XPATH,'//input[@id="name"]').send_keys(Name)
    driver.find_element(By.XPATH,'//input[@id="alertbtn"]').click()
    time.sleep(2)
    alerts = driver.switch_to.alert
    alert_text = alerts.text
    print(alert_text)
    assert Name in alert_text
    alerts.accept()
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="confirmbtn"]').click()
    time.sleep(1)
    alerts.dismiss()
    time.sleep(1)
# alert()

'''Wait Practice'''

