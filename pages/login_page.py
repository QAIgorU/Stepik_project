from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #assert "who_run_the_word" in self.browser.current_url, "'login' not in current url" #для проверки что тест может отработать с ошибкой
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password, browser):
        input1 = browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        input1.send_keys(email)
        print(email)
        time.sleep(2)
        input2 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        input2.send_keys(password)
        print(password)
        time.sleep(2)
        input3 = browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        input3.send_keys(password)
        print(password)
        time.sleep(2)
        button_register = browser.find_element(By.CSS_SELECTOR, "#register_form .btn-primary")
        print(button_register.text)
        button_register.click()
        time.sleep(6)
