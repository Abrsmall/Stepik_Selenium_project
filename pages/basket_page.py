from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Basket is not empty"

    def check_message_in_all_languages(self, message_options, language, msg):
        assert language in message_options and message_options.get(language) == msg, "Error in the text message"

    def validation_empty_basket_msg(self, message_options):
        try:
            msg = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text
            shopping_link = self.browser.find_element(*BasketPageLocators.LANG).text
            msg = msg.split(f' {shopping_link}')[0]
            lang = self.get_language()
            self.check_message_in_all_languages(message_options, lang, msg)
        except NoSuchElementException:
            'Empty basket msg not found'

    def get_language(self):
        elem = self.browser.find_element(*BasketPageLocators.LANG)
        language = elem.get_attribute("href")
        language = language.split('/')[-2]
        return language
