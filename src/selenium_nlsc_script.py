from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import re

class SeleniumNLSC:
    def __init__(self):
        # Options
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Initialize the Selenium WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("https://maps.nlsc.gov.tw/T09/mapshow.action")

    def close_notification(self):
        self.driver.implicitly_wait(5)
        close1 = self.driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/button")
        close1.click()
        close2 = self.driver.find_element(By.XPATH, "/html/body/div[25]/div[1]/button")
        close2.click()
        collapseCoord = self.driver.find_element(By.XPATH, '//*[@id="map_header"]/div[4]/ul[3]/li/a')
        collapseCoord.click()

    def get_nlsc_data(self, mat):
        
        nlsc_collection = []

        for arr in mat:

            nlsc_data = []
            real_areaOffice = ''
            output_string = ''

            try:
                # get btn
                time.sleep(1.0)
                self.driver.implicitly_wait(3)
                city_element = self.driver.find_element(By.ID, 'city')
                city = Select(city_element)
                areaOffice_element = self.driver.find_element(By.ID, 'area_office')
                areaOffice = Select(areaOffice_element)
                # section_code = self.driver.find_element(By.ID, 'sectioncode')
                section_code = self.driver.find_element(By.XPATH, '//*[@id="sectioncode"]')
                
                land_code = self.driver.find_element(By.ID, 'landcode')
                query_btn = self.driver.find_element(By.ID, 'div_cross_query')
                pos_btn1 = self.driver.find_element(By.ID, 'pos_li_1')
                pos_btn2 = self.driver.find_element(By.ID, 'pos_li_2')
                # fill in data            
                city.select_by_visible_text(arr[0].replace('台', '臺'))
                # areaOffice.select_by_visible_text(arr[1])
                section_code.clear()
                land_code.clear()   
                section_code.send_keys(arr[1])
                land_code.send_keys(arr[2])
                
                time.sleep(1.5)
                real_areaOffice = areaOffice.first_selected_option.text

                # search and close notification
                query_btn.click()
                try:
                    close3 = self.driver.find_element(By.XPATH, "/html/body/div[26]/div[1]/button")
                    close3.click()
                except:
                    pass

                
                detail_btn = self.driver.find_element(By.XPATH, '//span[@id="div_cross"]/input[1]')
                detail_btn.click()

                time.sleep(1.5)

                landpos_data = self.driver.find_element(By.ID, 'LandPos_Data')
                # Replace multiple spaces with a single space
                input_string = landpos_data.get_attribute('textContent')
                output_string = re.sub(r'\s+', ';', input_string)
                print(output_string)
            except:
                pass

            nlsc_data.append(real_areaOffice)
            nlsc_data.append(output_string)
            nlsc_collection.append(nlsc_data)

            # # get basic data
            # basic_table = self.driver.find_element(By.XPATH, '//*[@id="qryLand_tab1"]/table/tbody/tr[1]/td')
            # print(basic_table.get_attribute('textContent'))
            
            # # get land data
            # land_table = self.driver.find_element(By.XPATH, '//*[@id="qryLand_tab2_0"]/table')
            # print(land_table.get_attribute('textContent'))
            

            # reset the page
            pos_btn2.click()
            time.sleep(0.5)
            pos_btn1.click()
        # while True:
        #     continue     

        return nlsc_collection 


    def open_website(self):
        # Open the specified website
        self.driver.get(self.url)

    def perform_search(self, search_query):
        # Find the search input element and enter the search query
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    def print_results(self):
        # Print the titles of the search results
        search_results = self.driver.find_elements(By.CSS_SELECTOR, 'h3')
        for result in search_results:
            print(result.text)

    def close_browser(self):
        # Close the browser window
        self.driver.quit()


    def get_nlsc_data_new(self, mat):
        
        nlsc_collection = []

        for arr in mat:

            nlsc_data = []
            real_areaOffice = ''
            output_string = ''

            try:
                # get btn
                # time.sleep(1.0)
                self.driver.implicitly_wait(3)
                city_element = self.driver.find_element(By.ID, 'city')
                city = Select(city_element)
                areaOffice_element = self.driver.find_element(By.ID, 'area_office')
                areaOffice = Select(areaOffice_element)
                # section_code = self.driver.find_element(By.ID, 'sectioncode')
                section_code = self.driver.find_element(By.XPATH, '//*[@id="sectioncode"]')
                
                land_code = self.driver.find_element(By.ID, 'landcode')
                query_btn = self.driver.find_element(By.ID, 'div_cross_query')
                pos_btn1 = self.driver.find_element(By.ID, 'pos_li_1')
                pos_btn2 = self.driver.find_element(By.ID, 'pos_li_2')
                # fill in data            
                city.select_by_visible_text(arr[0].replace('台', '臺'))
                # areaOffice.select_by_visible_text(arr[1])
                section_code.clear()
                land_code.clear()   
                section_code.send_keys(arr[1])
                land_code.send_keys(arr[2])
                
                time.sleep(0.5)
                real_areaOffice = areaOffice.first_selected_option.text

                # search and close notification
                query_btn.click()
                try:
                    close3 = self.driver.find_element(By.XPATH, "/html/body/div[26]/div[1]/button")
                    close3.click()
                except:
                    pass

                
                # detail_btn = self.driver.find_element(By.XPATH, '//span[@id="div_cross"]/input[1]')
                # detail_btn.click()

                # time.sleep(1.5)

                # landpos_data = self.driver.find_element(By.ID, 'LandPos_Data')
                # # Replace multiple spaces with a single space
                # input_string = landpos_data.get_attribute('textContent')
                # output_string = re.sub(r'\s+', ';', input_string)
                # print(output_string)
            except:
                pass

            # nlsc_data.append(real_areaOffice)
            # nlsc_data.append(output_string)
            # nlsc_collection.append(nlsc_data)

            # # get basic data
            # basic_table = self.driver.find_element(By.XPATH, '//*[@id="qryLand_tab1"]/table/tbody/tr[1]/td')
            # print(basic_table.get_attribute('textContent'))
            
            # # get land data
            # land_table = self.driver.find_element(By.XPATH, '//*[@id="qryLand_tab2_0"]/table')
            # print(land_table.get_attribute('textContent'))
            

            # reset the page
            # pos_btn2.click()
            # time.sleep(0.5)
            # pos_btn1.click()
        while True:
            continue     

        return nlsc_collection 

# Example usage:
# if __name__ == "__main__":
#     # Replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable
#     # Replace 'https://www.google.com' with the URL of the website you want to interact with
#     selenium_example = SeleniumNLSC(driver_path='path_to_chromedriver', url='https://www.google.com')

#     # Open the website
#     selenium_example.open_website()

#     # Perform a search
#     selenium_example.perform_search('Selenium example')

#     # Print the search results
#     selenium_example.print_results()

#     # Close the browser
#     selenium_example.close_browser()
