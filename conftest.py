import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.screenshot import take_screenshot


@pytest.fixture
def driver(request):
    browser = getattr(request, "param", "chrome")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
    elif browser == "firefox":
        options = FirefoxOptions()
    else:
        raise Exception(f"Browser {browser} is not supported")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            test_name = item.name
            screenshot_path = take_screenshot(driver, test_name)

            if os.path.exists(screenshot_path):
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=test_name,
                        attachment_type=allure.attachment_type.PNG
                    )