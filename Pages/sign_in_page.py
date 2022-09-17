from selenium.webdriver.common.by import By
from Pages.sign_page import SignPage
from conftest import driver
from constants import *
import pytest


@pytest.mark.usefixtures("setup_teardown")
class SignInPage(SignPage):

    EMAIL_NOT_FOUND_MESSAGE = "Apologies, but we couldn’t find your e-mail address. Get a Free Trial"
    INVALID_EMAIL_MESSAGE = "Invalid email address try again or Get a Free Trial"

    def __init__(self):
        super().__init__()
        driver.get(SIGN_IN_PAGE)

    def email_input(self):
        return driver.find_element(By.ID, "input19")

    def login_button(self):
        return driver.find_element(By.CLASS_NAME, "btn btn-blue btn-lwide")

    def invalid_email_error_message(self):
        return driver.find_element(By.CLASS_NAME, "error-message").text

    def free_trail_button(self):
        return driver.find_element(By.CLASS_NAME, "btn btn-small")
