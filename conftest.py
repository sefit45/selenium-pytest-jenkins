import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import time
import pytest_html


@pytest.fixture
def driver(request):
    browser = request.param if hasattr(request, "param") else "chrome"

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

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshots_dir = "screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        test_name = request.node.name
        file_name = f"{test_name}_{browser}.png"
        file_path = os.path.join(screenshots_dir, file_name)

        driver.save_screenshot(file_path)

        if hasattr(request.node, "extras"):
            request.node.extras.append(pytest_html.extras.png(file_path))

        print(f"Screenshot saved: {file_path}")

    time.sleep(2)
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    if not hasattr(item, "extras"):
        item.extras = []

    rep.extras = item.extras
