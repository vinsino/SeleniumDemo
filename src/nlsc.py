from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
driver.maximize_window()
driver.get("https://maps.nlsc.gov.tw/T09/mapshow.action")

title = driver.title

driver.implicitly_wait(5)

close1 = driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/button")
close1.click()
close2 = driver.find_element(By.XPATH, "/html/body/div[25]/div[1]/button")
close2.click()

collapseCoord = driver.find_element(By.XPATH, '//*[@id="map_header"]/div[4]/ul[3]/li/a')
collapseCoord.click()

# closes = driver.find_elements(By.CSS_SELECTOR, ".ui-button.ui-corner-all.ui-widget.ui-button-icon-only.ui-dialog-titlebar-close")
# print(len(closes))

# class="ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close"

city_element = driver.find_element(By.ID, 'city')
city = Select(city_element)
city_list = city.options
city.select_by_visible_text('新北市')

# city.select_by_value('C')

areaOffice_element = driver.find_element(By.ID, 'area_office')
areaOffice = Select(areaOffice_element)
selected_option_list = areaOffice.options
areaOffice.select_by_visible_text('汐止區')

section_code = driver.find_element(By.ID, 'sectioncode')
section_code.send_keys('1038')

land_code = driver.find_element(By.ID, 'landcode')
land_code.send_keys('1-0')

query_btn = driver.find_element(By.ID, 'div_cross_query')
query_btn.click()

close3 = driver.find_element(By.XPATH, "/html/body/div[26]/div[1]/button")
close3.click()

detail_btn = driver.find_element(By.XPATH, '//span[@id="div_cross"]/input[1]')
detail_btn.click()

query_table = driver.find_element(By.XPATH, '//*[@id="qryLand_tab1"]/table/tbody/tr[1]/td')
print(query_table.get_attribute('textContent'))

# /html/body/div[23]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div[2]/ul/table/tr[1]/td/span/input[1]
# //*[@id="div_cross"]/input[1]

# city.select_by_value('C')


# print(len(selected_option_list))

# for e in selected_option_list:
#         print(e.get_attribute("textContent"))

# elements = driver.find_elements(By.CLASS_NAME, 'title')

# for e in elements:
#     if ("地籍圖" in e.get_attribute("textContent")):
#         parent = e.parent
#         print(e.get_attribute("textContent"))


# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text
print(title)

while(True):
    pass

driver.quit()
