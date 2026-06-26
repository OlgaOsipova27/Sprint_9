from selenium.webdriver.common.by import By

class RecipeCardLocators:
    CARD = (By.CSS_SELECTOR, "div.style_card__1Le2w")
    TITLE_LINK = (By.CSS_SELECTOR, "div.style_card__body__3mEB4 a.style_card__title__1iaT0")
    LOGOUT_LINK = (By.LINK_TEXT, "Выход")

    @staticmethod
    def get_card_by_title(title):
        return (By.XPATH, f"//a[text()='{title}']")
