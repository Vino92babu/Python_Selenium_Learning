import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    # Chrome Configuration
    options = Options()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    # Separate Chrome profile
    options.add_argument(
        r"--user-data-dir=C:\Selenium\ChromeProfile"
    )

    # Launch Chrome
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    # Give driver to test
    yield driver

    # Close browser after test
    driver.quit()