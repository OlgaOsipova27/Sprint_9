import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome"])
def driver():

    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()