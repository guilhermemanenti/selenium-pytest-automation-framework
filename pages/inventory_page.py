from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def go_to_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()
