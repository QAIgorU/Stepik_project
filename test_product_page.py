from .pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('promo_offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")), "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.guest_can_see_product_name()
    time.sleep(2)
    page.product_price_is_correct()


