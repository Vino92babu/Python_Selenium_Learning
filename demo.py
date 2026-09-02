from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
driver.maximize_window()
driver.get("https://www.google.com")

print("Title:", driver.title)

<<<<<<< HEAD
driver.quit()
=======
driver.quit()....
>>>>>>> 9338615aedea9414858d876414363a993e1bbe20
