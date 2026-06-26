import allure
from pages.registration_page import RegistrationPage
from pages.base_page import BasePage
from pages.main_page import MainPage

from locators.login_page_locators import LogiPageLocators as loginloc
from locators.main_page_locators import RecipeCardLocators as mainloc

class LoginPage(BasePage):


    @allure.step("Регистрация и вход")
    def login(self):

        registration = RegistrationPage(self.driver)
        login_data = registration.registration()

        login = login_data["username"]
        password = login_data["password"]

        main_page = MainPage(self.driver)
        main_page.open_signin_page()

        self.click_element(loginloc.INPUT_EMAIL)
        self.fill_input(loginloc.INPUT_EMAIL, login)

        self.click_element(loginloc.INPUT_PASSWORD)
        self.fill_input(loginloc.INPUT_PASSWORD, password)

        self.click_element(loginloc.BUTTON_ENTER_MAIN)

        self.wait_for_element(mainloc.LOGOUT_LINK)

    @allure.step("Кнопка 'Выход' отображается")
    def is_button_exit_displayed(self):
        
        element = self.wait_for_visible_element(mainloc.LOGOUT_LINK, timeout=5)
        return element.is_displayed()
    
    @allure.step("Форма входа отображается")
    def is_auth_form_displayed(self):

        element = self.wait_for_visible_element(loginloc.AUTH_FORM, timeout=5)
        return element.is_displayed()