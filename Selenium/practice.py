import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()


'''Browser's url'''
def browser(url):
    driver.get(url)
    # driver.maximize_window()
    time.sleep(2)


'''input text'''
def login_page():
    browser("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("rahulshettyacademy")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("Learning@830$3mK2")
# login_page()

'''DropDown - their are two types of DropDown - Static / Auto_Suggestive '''

def DropDown_Static():
    browser("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("rahulshettyacademy")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("Learning@830$3mK2")
    Select(driver.find_element(By.XPATH, '//select[@class="form-control"]')).select_by_value("teach")
    Select(driver.find_element(By.XPATH, '//select[@class="form-control"]')).select_by_index(0)
    Select(driver.find_element(By.XPATH, '//select[@class="form-control"]')).select_by_visible_text("Consultant")
# DropDown_Static()

def DrpDown_Auto_Suggestive():
    browser("https://rahulshettyacademy.com/dropdownsPractise/")
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
    browser("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']").click()
    assert driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']").is_selected()
# Checkbox_Static()

def Checkbox_Dynamic():
    browser("https://rahulshettyacademy.com/AutomationPractice/")
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
    browser("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element(By.XPATH,'//input[@value="radio1"]').click()
    assert driver.find_element(By.XPATH,'//input[@value="radio1"]').is_selected()
# Radio_btn_static()

def Radio_btn_dynamic():
    browser("https://rahulshettyacademy.com/AutomationPractice/")
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
    browser("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element(By.XPATH,'//input[@id="displayed-text"]').is_displayed()
    assert driver.find_element(By.XPATH,'//input[@id="displayed-text"]').is_displayed()
    driver.find_element(By.XPATH, '//input[@id="hide-textbox"]').click()
    # assert driver.find_element(By.XPATH, '//input[@id="displayed-text"]').is_displayed()
    assert not driver.find_element(By.XPATH, '//input[@id="displayed-text"]').is_displayed()
# isdisplayed()

'''Alerts'''
Name = "Vinoth"
def alert():
    browser("https://rahulshettyacademy.com/AutomationPractice/")
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
def waits():
    driver.implicitly_wait(2)
    browser("https://rahulshettyacademy.com/seleniumPractise/#/")
    page_title = driver.title
    assert page_title == "GreenKart - veg and fruits kart"
    search_box = driver.find_element(By.CSS_SELECTOR,'input[class="search-keyword"]')
    search_box.send_keys("be")
    search_button = driver.find_element(By.CSS_SELECTOR, 'button[class="search-button"]')
    search_button.click()
    time.sleep(2)

    # validating on items displayed.
    expected_list = ['Cucumber - 1 Kg','Beetroot - 1 Kg','Beans - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
    actual_list = []
    total_list= driver.find_elements(By.XPATH,'//div/h4[@class="product-name"]')
    for list in total_list:
        actual_list.append(list.text)
    assert expected_list == actual_list

    total_products = driver.find_elements(By.CSS_SELECTOR,'div[class="product"]')
    total_products_count = len(total_products)
    print(total_products_count)
    assert total_products_count >0
    # add_cart_btn = driver.find_elements(By.XPATH,'//div[@class="product"]/div/button')
    count =0
    for product in total_products:
        product.find_element(By.XPATH,'div/button').click()
        count = count + 1
    print(count)
    # assert count == total_products_count
    item = driver.find_element(By.XPATH,'//tbody/tr[1]/td/strong')
    item_count = int(item.text)
    print(item_count)
    assert item_count == count == total_products_count
    Cart_btn = driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]')
    Cart_btn.click()
    # time.sleep(2)
    chk_out_btn = driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]')
    chk_out_btn.click()
    # time.sleep(5)
    apply_promo_text = driver.find_element(By.CSS_SELECTOR, '.promoCode')
    apply_promo_text.send_keys("rahulshettyacademy")
    # time.sleep(1)
    apply_btn = driver.find_element(By.CSS_SELECTOR,'.promoBtn')
    apply_btn.click()
    # time.sleep(5)
    wait = WebDriverWait(driver,15)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
    succ_promo_text = driver.find_element(By.CLASS_NAME, 'promoInfo')
    print(succ_promo_text.text)
    assert succ_promo_text.text == "Code applied ..!"

#other Validations
    total_price = driver.find_elements(By.XPATH,'//td[5]/p[@class="amount"]')
    total_sum = 0
    for total_item_price in total_price:
        price = int(total_item_price.text)
        # print(price)
        total_sum = total_sum + price
    print(total_sum)
    total_Amount = int(driver.find_element(By.XPATH,'//span[@class="totAmt"]').text)
    # if total_sum == total_Amount:
    #     print("Total Amount is gets matched with total price")
    # else:
    #     print("recount the item")
    assert total_sum == int(total_Amount), "gets matched"
    total_discount = driver.find_element(By.XPATH,'//span[@class="discountPerc"]')
    discount = int(total_discount.text.replace('%',''))
    final_price = (total_Amount/100)*discount
    print("final_price: " ,final_price,type(final_price))
    print("Total_amount:", total_Amount,type(total_Amount))
    final_prices = (total_Amount - final_price)
    print("final_price",final_prices,type(final_prices))
    total_discount_amount = driver.find_element(By.XPATH,'//span[@class="discountAmt"]').text
    place_order_btn = driver.find_element(By.LINK_TEXT,'Place Order')
    print("Calculated final price:", repr(final_prices))
    print("Displayed final price:", repr(float(total_discount_amount)))
    assert round(float(final_prices), 2) == round(total_discount_amount, 2)
    place_order_btn.click()
waits()

