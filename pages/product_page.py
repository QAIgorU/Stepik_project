from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def guest_can_see_product_name(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        print(product_name_in_basket.text)
        print(product_name_in_store.text)
        assert product_name_in_store.text in product_name_in_basket.text, "Product name is no the same"

    def product_price_is_correct(self):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET)
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_STORE)
        print(product_price_in_basket.text)
        print(product_prise_in_store.text)
        assert product_prise_in_store.text in product_price_in_basket.text, "Price is wrong"

