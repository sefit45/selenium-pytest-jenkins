import pytest
from selenium import webdriver
import os
import pytest_html


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    if request.node.rep_call.failed:
        screenshots_dir = "screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        test_name = request.node.name
        file_name = f"{test_name}.png"
        file_path = os.path.join(screenshots_dir, file_name)

        driver.save_screenshot(file_path)

        if hasattr(request.node, "extras"):
            request.node.extras.append(pytest_html.extras.png(file_path))

        print(f"Screenshot saved: {file_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    if not hasattr(item, "extras"):
        item.extras = []

    rep.extras = item.extras