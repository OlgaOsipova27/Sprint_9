from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.driver = browser

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_visible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    def wait_for_url_changes(self, old_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_changes(old_url)
        )


    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        self.scroll_to_element(element)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def click_element_js(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def fill_input(self, locator, text):
        element = self.wait_for_visible_element(locator)
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(text)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()
    
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_presence_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def open_url(self, url):

        return self.driver.get(url)

    