from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    BUTTON_AGREE_POLITIC = (By.CSS_SELECTOR, "div.pull-right > input:nth-child(3)")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "div.pull-right > input.btn.btn-primary:nth-child(4)")

    def registration(self):
        self.write(self.INPUT_FIRSTNAME, "test")
        self.write(self.INPUT_LASTNAME, "test")
        self.write(self.INPUT_EMAIL, "testtest@mail.ru")
        self.write(self.INPUT_TELEPHONE, "88005553535")
        self.write(self.INPUT_PASSWORD, "TeStPaSsWoRd")
        self.write(self.INPUT_CONFIRM, "TeStPaSsWoRd")
        self.click(self.BUTTON_AGREE_POLITIC)
        self.click(self.BUTTON_LOGIN)
