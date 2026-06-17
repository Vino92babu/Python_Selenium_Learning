from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())  jb
)

driver.maximize_window()
driver.get("https://www.google.com")

print("Title:", driver.title)

driver.quit()