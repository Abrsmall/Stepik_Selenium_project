from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PASS = (By.NAME, 'login-password')
    LOGIN_BTN = (By.NAME, 'login_submit')
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASS = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASS = (By.ID, 'id_registration-password2')
    REGISTER_BTN = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'article div h1')
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, '#messages :nth-child(1) div strong')
    PRICE = (By.CSS_SELECTOR, 'article div p')
    PRICE_OF_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(3) div strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, '.basket-mini span a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    LANG = (By.CSS_SELECTOR, '#content_inner a')
