from selenium.webdriver.common.by import By

class CreateAccountLocators:

    INPUT_NAME = (By.CSS_SELECTOR, "input[name='first_name']")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input[name='last_name']")
    INPUT_USER_NAME = (By.CSS_SELECTOR, "input[name='username']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")

    REGISTRATION_HEADER = (By.XPATH, "//h1[text()='Регистрация']")
