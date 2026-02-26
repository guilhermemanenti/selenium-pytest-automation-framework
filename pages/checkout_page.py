from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_information(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FINISH_BUTTON))
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_success_message(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    def get_complete_message(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.COMPLETE_MESSAGE))
        return self.driver.find_element(*self.COMPLETE_MESSAGE).text
