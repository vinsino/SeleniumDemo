from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SeleniumExample:
    def __init__(self, driver_path, url):
        # Initialize the Selenium WebDriver
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.url = url        

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

# Example usage:
if __name__ == "__main__":
    # Replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable
    # Replace 'https://www.google.com' with the URL of the website you want to interact with
    selenium_example = SeleniumExample(driver_path='path_to_chromedriver', url='https://www.google.com')

    # Open the website
    selenium_example.open_website()

    # Perform a search
    selenium_example.perform_search('Selenium example')

    # Print the search results
    selenium_example.print_results()

    # Close the browser
    selenium_example.close_browser()
