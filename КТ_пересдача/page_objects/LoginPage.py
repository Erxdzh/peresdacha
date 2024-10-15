from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "form:nth-child(3) > input.btn.btn-primary:nth-child(3)")

    def correct_logging(self):
        self.write(self.INPUT_EMAIL, "testtest@mail.ru")
        self.write(self.INPUT_PASSWORD, "TeStPaSsWoRd")
        self.click(self.BUTTON_LOGIN)

    def incorrect_logging(self):
        self.write(self.INPUT_EMAIL, "incorrect@mail.ru")
        self.write(self.INPUT_PASSWORD, "uncorrectedPassword")
        self.click(self.BUTTON_LOGIN)
