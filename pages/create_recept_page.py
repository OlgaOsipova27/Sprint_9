import allure

from locators.create_recept_locators import CreateReceptLocators as createloc
from locators.main_page_locators import RecipeCardLocators
from pages.base_page import BasePage
from data.data_for_test import generate_recept_data, TIME, WEIGHT, INGRIDIENT

from config import file_path


class CreateReceptPage(BasePage):
 
    @staticmethod
    def get_recept_data():

        return generate_recept_data()
 
    @allure.step("Ввод названия рецепта")
    def input_name(self, recept_data):

        name_recept = recept_data["name_recept"]
        self.click_element(createloc.INPUT_NAME_OF_RECEPT)
        self.fill_input(createloc.INPUT_NAME_OF_RECEPT, name_recept)
        
        self._recipe_name = name_recept
 
    @allure.step('Выбор тега')
    def select_tag(self):

        self.click_element(createloc.CHECKBOX_ORANGE)
 
    @allure.step("Ввод вемени приготовления")
    def input_time(self):

        self.click_element(createloc.TIME_INPUT)
        self.fill_input(createloc.TIME_INPUT, TIME)
 
    @allure.step("Ввод ингридиентов")
    def input_ingridients(self):

        self.click_element(createloc.INGREDIENTS_INPUT)
        self.fill_input(createloc.INGREDIENTS_INPUT, INGRIDIENT)
        self.wait_for_visible_element(createloc.INGREDIENT_DROPDOWN) 
        self.click_element(createloc.SELECT_SALAT)
        self.click_element(createloc.INGREDIENT_AMOUNT_INPUT)
        self.fill_input(createloc.INGREDIENT_AMOUNT_INPUT, WEIGHT)
        self.click_element(createloc.ADD_INGREDIENT_BUTTON)
    
    @allure.step("Ввод описания рецепта")
    def description_input(self, recept):

        description = recept["description"]
        self.click_element(createloc.DESCRIPTION_FIELD)
        self.fill_input(createloc.DESCRIPTION_FIELD, description)
 
    @allure.step("Загрузка файла")
    def upload_file(self):

        self.wait_for_presence_element(createloc.FILE_INPUT)
        self.find_element(createloc.FILE_INPUT).send_keys(str(file_path))

    @allure.step("Заполнение формы создания рецепта")
    def create_recipe(self):
        
        self.click_element(createloc.CREATE_RECIPE_LINK_MAIN)
        self.wait_for_visible_element(createloc.INPUT_NAME_OF_RECEPT)

        recept_data = self.get_recept_data()
        
        self.input_name(recept_data)
        self.select_tag()
        self.input_time()
        self.input_ingridients()
        self.description_input(recept_data)
        self.upload_file()
        self.click_element(createloc.CREATE_RECIPE_BUTTON)
        
        return self._recipe_name
 
    @allure.step("Проверка, что карточка рецепта отображается на главной странцие")
    def is_recipe_card_displayed(self, title: str) -> bool:
        
        card_locator = RecipeCardLocators.get_card_by_title(title)
        try:
            element = self.wait_for_visible_element(card_locator, timeout=10)
            return element.is_displayed()
        except:
            return False
        
    @allure.step("Получение названия карточки рецепта")
    def get_recipe_title_text(self, title: str) -> str:
        
        card_locator = RecipeCardLocators.get_card_by_title(title)
        element = self.wait_for_visible_element(card_locator, timeout=10)
        return element.text
