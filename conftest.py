import pytest
from constants import *
from selenium import webdriver
from Utilities.logger import get_logger
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
logger = get_logger()


def pytest_addoption(parser):
    parser.addoption("--headless_mode", action="store", default=False, type=bool)


def setup():
    logger.info("Starting setup")


def teardown():
    logger.info("Starting teardown")


@pytest.fixture(scope="session")
def setup_teardown():
    setup()
    yield
    teardown()


def pytest_sessionstart(session):
    logger.info("Starting session")
    logger.info("Opening main page")
    if session.config.option.headless_mode:
        webdriver.ChromeOptions().headless = True  # TODO - doesn't work - requires a fix!!!
    driver.get(MAIN_VICARIUS_PAGE)
    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)


def pytest_sessionfinish():
    logger.info("Finishing session")
    driver.quit()
