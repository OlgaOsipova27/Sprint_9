import allure

from locators.create_account_locators import CreateAccountLocators as accountloc
from locators.login_page_locators import LogiPageLocators as loginloc

from data.data_for_test import generate_user_data

from pages.base_page import BasePage
from pages.main_page import MainPage

class RegistrationPage(BasePage):
    
    @staticmethod
    def get_user_data():

        return generate_user_data()

    @allure.step("Открытие страницы регистрации")
    def open_registration_page(self):

        main_page = MainPage(self.driver)
        main_page.open_signin_page()

        self.click_element(loginloc.BUTTON_CREATE_ACCOUNT)
        self.wait_for_element(accountloc.REGISTRATION_HEADER)

    @allure.step("Ввод имени")
    def input_name(self, data):

        name = data["name"]

        self.click_element(accountloc.INPUT_NAME)
        self.fill_input(accountloc.INPUT_NAME, name)
        self.user_name = name

    @allure.step("Ввод фамилии")
    def input_surname(self, data):

        surname=data["surname"]
        self.click_element(accountloc.INPUT_SURNAME)
        self.fill_input(accountloc.INPUT_SURNAME, surname)
        self.user_surname = surname

    @allure.step("Ввод имени пользователя")
    def input_username(self, data):

        username = data["username"]
        self.click_element(accountloc.INPUT_USER_NAME)
        self.fill_input(accountloc.INPUT_USER_NAME, username)
        self.username = username

    @allure.step("Ввод email")
    def input_email(self, data):

        email = data["email"]
        self.click_element(accountloc.INPUT_EMAIL)
        self.fill_input(accountloc.INPUT_EMAIL, email)
        self.email = email

    @allure.step("Ввод пароля")
    def input_password(self, data):
        
        password = data["password"]
        self.click_element(accountloc.INPUT_PASSWORD)
        self.fill_input(accountloc.INPUT_PASSWORD, password)
        self.password = password

    @allure.step("Ввод данных в поля формы регистрации")
    def registration(self):

        self.open_registration_page()

        data = self.get_user_data()

        self.input_name(data)
        self.input_surname(data)
        self.input_username(data)
        self.input_email(data)
        self.input_password(data)

        self.click_element(accountloc.CREATE_ACCOUNT_BUTTON)
        self.wait_for_element(loginloc.AUTH_FORM)

        return {
            "name": self.user_name,
            "surname": self.user_surname,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

         