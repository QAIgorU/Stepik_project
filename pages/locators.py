from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alertinner")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info p:first-child")
    PRODUCT_PRICE_STORE = (By.CSS_SELECTOR, ".price_color")

    #пустая строка