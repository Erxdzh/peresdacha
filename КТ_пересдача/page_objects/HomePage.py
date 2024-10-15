from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    INPUT_SEARCH = (By.CSS_SELECTOR, "div.input-group > input.form-control.input-lg")