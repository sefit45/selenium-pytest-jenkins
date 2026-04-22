from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WikipediaPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.wikipedia.org/")

    def search_for(self, text):
        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)

    def get_main_heading(self):
        heading = self.wait.until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
        return heading.text