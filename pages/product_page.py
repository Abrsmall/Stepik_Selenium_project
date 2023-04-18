from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_name_added_to_basket(self):
        product_name_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        return product_name_alert

    def get_price_of_product(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def get_price_of_basket(self):
        price_of_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text
        return price_of_basket
