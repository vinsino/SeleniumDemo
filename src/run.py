from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to the ChromeDriver executable
chrome_driver_path = './chromedriver-win64/chromedriver.exe'  # Replace with the actual path
service = Service(executable_path=chrome_driver_path)
# Initialize the Chrome WebDriver with the specified path
print(service.service_url)
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()

# Now you can use 'driver' to automate Chrome
driver.get("https://www.google.com.tw/?hl=zh_TW")
title = driver.title
print(title)

driver.implicitly_wait(5.5)