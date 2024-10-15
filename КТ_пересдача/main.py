from conftest import *
from page_objects.HomePage import HomePage
from page_objects.LoginPage import LoginPage
from page_objects.RegistrationPage import RegistrationPage


@allure.feature("Функциональность входа")
@allure.title("Тест на успешный вход в аккаунт")
@allure.description("Этот тест проверяет, что пользователь может успешно войти в систему с корректными учетными данными.")
def test_logging(driver):
    driver.get("https://demo-opencart.ru/index.php?route=account/login")
    LoginPage(driver).correct_logging()
    LoginPage(driver).take_screenshot()


@allure.feature("Функциональность входа")
@allure.title("Тест на вход с некорректными учетными данными")
@allure.description("Этот тест проверяет, как система реагирует на попытку входа с некорректными данными.")
def test_incorrect_logging(driver):
    driver.get("https://demo-opencart.ru/index.php?route=account/login")
    LoginPage(driver).incorrect_logging()
    LoginPage(driver).take_screenshot()


@allure.feature("Регистрация аккаунта")
@allure.title("Тест на регистрацию нового аккаунта")
@allure.description("Этот тест проверяет, что новый аккаунт может быть успешно зарегистрирован.")
def test_registration(driver):
    driver.get("https://demo-opencart.ru/index.php?route=account/register")
    RegistrationPage(driver).registration()
    RegistrationPage(driver).take_screenshot()


@allure.feature("Регистрация аккаунта")
@allure.title("Тест на повторную регистрацию с уже существующим логином")
@allure.description("Этот тест проверяет, как система реагирует на попытку регистрации с уже существующим email.")
def test_again_registration(driver):
    driver.get("https://demo-opencart.ru/index.php?route=account/register")
    RegistrationPage(driver).registration()
    RegistrationPage(driver).take_screenshot()


@allure.feature("Функциональность поиска")
@allure.title("Тест поиска по ключевым словам")
@allure.description("Этот тест проверяет, что поиск по ключевому слову 'iphone' возвращает релевантные результаты.")
def test_searching(driver):
    HomePage(driver).write(HomePage.INPUT_SEARCH, "iphone")
    HomePage(driver).enter()
    HomePage(driver).take_screenshot()


@allure.feature("Функциональность поиска")
@allure.title('Тест поиска при отсутствии результатов')
@allure.description("Этот тест проверяет, как система реагирует, когда по запросу не найдено результатов.")
def test_null_searching(driver):
    HomePage(driver).write(HomePage.INPUT_SEARCH, "test")
    HomePage(driver).enter()
    HomePage(driver).take_screenshot()
