from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    flash_message = login_page.get_flash_message()

    assert "You logged into a secure area!" in flash_message


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("tomsmith", "WrongPassword!")

    flash_message = login_page.get_flash_message()

    assert "Your password is invalid!" in flash_message