from selenium.webdriver.common.by import By

class LogiPageLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_ENTER_MAIN = (By.XPATH, "//h1[text()='Войти на сайт']/following-sibling::form//button[text()='Войти']")
    BUTTON_CREATE_ACCOUNT = (By.LINK_TEXT, "Создать аккаунт")

    AUTH_FORM = (By.XPATH, "//form[.//button[text()='Войти']]")
    

   