from selenium.webdriver.common.by import By

class CreateReceptLocators:
    CREATE_RECIPE_LINK_MAIN = (By.LINK_TEXT, "Создать рецепт")
    INPUT_NAME_OF_RECEPT = (By.XPATH, "(//input[contains(@class, 'styles_inputField')])[1]")
    CHECKBOX_ORANGE = (By.CSS_SELECTOR, "button[style*='background-color: orange']")
    INGREDIENTS_INPUT = (By.CSS_SELECTOR, "input.styles_ingredientsInput__1zzql")
    INGREDIENT_AMOUNT_INPUT = (By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    TIME_INPUT = (By.XPATH,"//label[.//div[normalize-space()='Время приготовления']]//input")

    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea.styles_textareaField__1wfhC")
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")

    # Контейнер выпадающего списка
    INGREDIENT_DROPDOWN = (By.CSS_SELECTOR, "div.styles_container__3ukwm")
    SELECT_SALAT = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]//div[text()='салат']")

