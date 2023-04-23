from .base_page import BasePage
from .locators import LoginPageLocators
import random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.browser.current_window_handle)
        assert 'login' in self.browser.current_url, 'Login link is not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def get_random_email(self, lenght=9):
        alfabet = 'abcdefghijklmnopqrstuvwxyz'
        email = ''.join(random.choice(alfabet) for i in range(lenght)) + '@mail.ru'
        return email

    def get_random_pass(self, lenght=9):
        alfabet = 'abcdefghijklmnopqrstuvwxyz'
        rndm = ''.join(random.choice(alfabet) for i in range(lenght))
        return rndm

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        register_pass = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        register_pass.send_keys(password)
        register_confirm_pass = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASS)
        register_confirm_pass.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
