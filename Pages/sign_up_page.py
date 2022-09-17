from selenium.webdriver.common.by import By
from Pages.sign_page import SignPage
from conftest import driver
from constants import *
import pytest


@pytest.mark.usefixtures("setup_teardown")
class SignUpPage(SignPage):

    PASSWORD_NOT_MATCHING_CRITERIA_ERROR_MESSAGE = "Must contain required characters."
    PERSONAL_EMAIL_ERROR_MESSAGE = "Can't be a personal email."
    INVALID_EMAIL_ERROR_MESSAGE = "Must be valid email address."
    FREE_TRAIL_HEADLINE = "Start Your\n30-day free trial"
    VALID_PASSWORD = "AAaa11!!"

    def __init__(self):
        super().__init__()
        driver.get(SIGN_UP_PAGE)

    def free_trail_headline(self):
        return driver.find_element(By.CLASS_NAME, "mb-4").text

    def work_email_input(self):
        return driver.find_element(By.ID, "input30")

    def personal_email_error(self):
        return driver.find_elements(By.XPATH, "//div[@class='error']")[2].text

    def password_input(self):
        return driver.find_element(By.ID, "input34")

    def password_error_message(self):
        # TODO - change xpath!
        # return driver.find_element(By.XPATH, "//div[@class='input-field is-error has-errors']")
        return driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div/div[2]/"
                                             "div[3]/div/div/form/div[1]/div[5]/div/div[2]")

    def password_must_contain_tags(self):
        return driver.find_element(By.XPATH, "//ul[@class='tags']")

    def login_button(self):
        return driver.find_element(By.CLASS_NAME, "btn btn-small")
