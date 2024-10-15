import datetime
import pytest
import logging
import allure
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    current_url = "https://demo-opencart.ru"

    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)

    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s starts at %s" % (request.node.name, datetime.datetime.now()))

    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception("Driver not supported")

    driver.test_name = request.node.name
    driver.logger = logger
    driver.log_level = log_level
    driver.get(current_url)
    driver.maximize_window()

    allure.attach(
        name=driver.session_id, body=json.dumps(driver.capabilities), attachment_type=allure.attachment_type.JSON
    )
    logger.info("Browser %s is opened" % browser)

    def fin():
        driver.quit()
        logger.info("===> Test %s ends at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
