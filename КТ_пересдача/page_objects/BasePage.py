import os

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.test_name = driver.test_name
        self.logger = driver.logger
        self.wait = WebDriverWait(self.driver, wait)
        self.action = ActionChains(self.driver)
        self.class_name = self.__class__.__name__
        self.logger.info(f"{self.class_name} initialized")

    def take_screenshot(self, screenshot_name="screenshot"):
        screenshot_name = self.test_name+"_"+screenshot_name
        screenshot_path = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        file_path = os.path.join(screenshot_path, f"{screenshot_name}.png")
        try:
            self.driver.save_screenshot(file_path)
            self.logger.info(f"Screenshot saved: {screenshot_name}")
            allure.attach.file(file_path, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")

    def element_name(self, element):
        for name, value in vars(self.__class__).items():
            if isinstance(value, (list, tuple)) and element in value:
                return f"{name}[{value.index(element)}]"
            elif value == element:
                return name
        return str(element)

    def find_element(self, element_locator):
        try:
            element = self.wait.until(ec.presence_of_element_located(element_locator))
            self.logger.info(f"Element found: {element_locator}")
            return element
        except Exception as e:
            self.logger.error(f"Element not found: {e}")
            raise e

    def click(self, element_locator):
        try:
            element_name = self.element_name(element_locator)
            self.wait.until(ec.element_to_be_clickable(element_locator)).click()
            self.logger.info(f"{self.class_name}: Clicked on '{element_name}'")
        except Exception as e:
            self.logger.error(f"Error clicking on element: {e}")
            raise e

    def enter_text(self, element_locator, value):
        try:
            element = self.find_element(element_locator)
            element_name = self.element_name(element_locator)
            element.clear()
            element.send_keys(value)
            self.logger.info(f"{self.class_name}: Entered '{value}' into '{element_name}'")
        except Exception as e:
            self.logger.error(f"Error entering text into element: {e}")
            raise e

    def write(self, element_locator, value):
        self.click(element_locator)
        self.enter_text(element_locator, value)

    def enter(self):
        self.action.send_keys(Keys.CONTROL).send_keys(Keys.ENTER).perform()
