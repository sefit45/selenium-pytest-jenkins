from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        username_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )

        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        login_button.click()

    def get_flash_message(self):
        flash = self.wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        return flash.text