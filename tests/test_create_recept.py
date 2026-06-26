import allure
from pages.create_recept_page import CreateReceptPage
from pages.main_page import MainPage

from pages.login_page import LoginPage

class TestCreateRecept:

    @allure.title("Проверка, что после создания рецепта карточка с рецептом отображается на главной странице")
    def test_after_create_recept_visible_card_of_recept(self, driver):

        login_page = LoginPage(driver)
        recept = CreateReceptPage(driver)
        main_page = MainPage(driver)

        login_page.login()
        recept_name = recept.create_recipe()
        main_page.open()

        assert recept.is_recipe_card_displayed(recept_name)

    
    @allure.title("Проверка, что после создания рецепта в карточке отображается именно то название, которое было задано при создании")
    def test_after_create_recept_recept_name_is_true(self, driver):

        login_page = LoginPage(driver)
        recept = CreateReceptPage(driver)
        main_page = MainPage(driver)

        login_page.login()
        recept_name = recept.create_recipe()
        main_page.open()


        assert recept.get_recipe_title_text(recept_name) == recept_name
