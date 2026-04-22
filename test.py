from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.wikipedia.org/")

search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "search"))
)

search_box.send_keys("Bitcoin")
search_box.send_keys(Keys.RETURN)

heading = wait.until(
    EC.presence_of_element_located((By.ID, "firstHeading"))
)

assert heading.text == "Bitcoin", f"Expected 'Bitcoin' but got '{heading.text}'"

print("Test passed successfully!")

input("Press Enter to close browser...")

driver.quit()