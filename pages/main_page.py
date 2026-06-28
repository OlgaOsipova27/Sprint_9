import allure

from data.url import URL_MAIN, URL_SIGNIN
from locators.main_page_locators import RecipeCardLocators as cardloc
from locators.login_page_locators import LogiPageLocators as loginloc
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step("Открыие главной страницы")
    def open(self):

        self.open_url(URL_MAIN)
        self.wait_for_visible_element(cardloc.CARD)

    @allure.step("Открыие страницв входа")
    def open_signin_page(self):
        
        self.open_url(URL_SIGNIN)
        self.wait_for_visible_element(loginloc.BUTTON_CREATE_ACCOUNT)
