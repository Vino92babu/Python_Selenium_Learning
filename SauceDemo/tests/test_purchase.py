from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_purchase(driver):

    wait = WebDriverWait(driver, 10)

    # Open application
    driver.get("https://www.saucedemo.com/")

    # Create page objects
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Login
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Verify Products page
    assert inventory_page.get_page_title() == "Products"

    # Add Backpack
    inventory_page.add_backpack()

    # Open Cart
    inventory_page.open_cart()

    # Verify Cart Product
    assert cart_page.get_product_name() == "Sauce Labs Backpack"

    # Checkout
    cart_page.click_checkout()

    # Enter Customer Information
    checkout_page.enter_customer_details(
        "Vinoth",
        "Babu",
        "600001"
    )

    # Continue
    checkout_page.click_continue()

    # Verify Checkout Overview
    assert checkout_page.get_page_title() == "Checkout: Overview"

    # Verify Product
    assert checkout_page.get_product_name() == "Sauce Labs Backpack"

    # Finish Order
    checkout_page.click_finish()

    # Verify Confirmation
    assert (
        checkout_page.get_confirmation_message()
        == "Thank you for your order!"
    )