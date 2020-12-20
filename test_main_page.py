from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


#def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.open() # открываем страницу
    #page.go_to_login_page() # метод из main_page ищет элемент по локатору и кликает на него


def test_guest_can_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


#def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #page = MainPage(browser, link)
    #page.open()
    #page.should_be_login_link() # сравнивает по локатору, что есть такой элемент (берет это все из main_page)


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.guest_can_go_to_basket_page()
    page.guest_cant_see_product_in_basket()
    page.guest_can_see_empty_basket()

    #пустая строка