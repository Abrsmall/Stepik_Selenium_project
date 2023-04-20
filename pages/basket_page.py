from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Basket is not empty"

    def empty_basket_msg(self):
        msg = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text
        shopping_link = self.browser.find_element(*BasketPageLocators.LANG).text
        msg = msg.split(f' {shopping_link}')[0]
        print(msg)
        return msg

    def get_language(self):
        elem = self.browser.find_element(*BasketPageLocators.LANG)
        language = elem.get_attribute("href")
        language = language.split('/')[-2]
        return language
