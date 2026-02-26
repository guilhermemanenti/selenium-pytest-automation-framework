from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    login_page.wait_for_inventory_page()

    assert "inventory" in driver.current_url

def test_login_invalid_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error_message = login_page.get_error_message()

    assert "Epic sadface" in error_message
