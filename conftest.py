import pytest
import allure
from utils.screenshot import take_screenshot


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            test_name = item.name

            screenshot_path = take_screenshot(driver, test_name)

            with open(screenshot_path, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name=test_name,
                    attachment_type=allure.attachment_type.PNG
                )