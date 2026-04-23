import pytest
import allure
from utils.screenshot import take_screenshot
from utils.logger import logger


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            test_name = item.name

            logger.error(f"Test Failed: {test_name}")

            screenshot_path = take_screenshot(driver, test_name)

            logger.info(f"Screenshot saved: {screenshot_path}")

            with open(screenshot_path, "rb") as file:
                allure.attach(
                    file.read(),
                    name=test_name,
                    attachment_type=allure.attachment_type.PNG
                )
