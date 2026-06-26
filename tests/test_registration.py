import allure

from pages.registration_page import RegistrationPage
from pages.base_page import BasePage
from pages.login_page import LoginPage

from data.url import URL_SIGNIN

class TestRegistration:

    @allure.title("Проверка, что после регистрации открывается страница входа")
    def test_after_registration_open_login_page(self, driver):
        
        base_page = BasePage(driver)
        registration_page = RegistrationPage(driver)
        
        registration_page.registration()
        url = base_page.get_current_url()

        assert url == URL_SIGNIN

    @allure.title("Проверка, что после регистрации отображается форма входа")
    def test_after_registration_enter_form_displayed(self, driver):

        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)

        registration_page.registration()
        assert login_page.is_auth_form_displayed()