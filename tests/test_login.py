import allure

from pages.login_page import LoginPage

from data.url import URL_MAIN


class TestLogin():

    @allure.title("Проверка, что после входа открывается главная страница с рецептами")
    def test_login_open_main_page(self, driver):

        login_page = LoginPage(driver)

        login_page.login()
        url = login_page.get_current_url()
 
        assert url == URL_MAIN

    @allure.title("Проверка, что после входа отображается кнопка 'Выход")
    def test_login_visible_button_exit(self, driver):

        login_page = LoginPage(driver)

        login_page.login()

        assert login_page.is_button_exit_displayed()





