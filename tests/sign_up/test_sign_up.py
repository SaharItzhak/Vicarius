import time

from selenium.common import NoSuchElementException
from Pages.sign_up_page import SignUpPage
from selenium.webdriver import Keys
from conftest import driver
from constants import *
import pytest


@pytest.mark.sign_up
class TestSignUp:
    """This group of tests are sanity tests for the sign-up page"""

    # This test will verify the title of the sign up page
    def test_start_free_trail(self):
        signUpPage = SignUpPage()
        assert signUpPage.free_trail_headline() == signUpPage.FREE_TRAIL_HEADLINE

    # This test will verify that when the user enters an email that
    # doesn't match email criteria, an error message will appear
    @pytest.mark.parametrize(
        ("password_inputs", "error_message"),
        (
            (INVALID_EMAIL, SignUpPage.INVALID_EMAIL_ERROR_MESSAGE),
            (PERSONAL_EMAIL, SignUpPage.PERSONAL_EMAIL_ERROR_MESSAGE),
        )
    )
    def test_email_not_matching_criteria(self, password_inputs, error_message):
        signUpPage = SignUpPage()
        signUpPage.work_email_input().send_keys(PERSONAL_EMAIL, Keys.RETURN)
        assert signUpPage.PERSONAL_EMAIL_ERROR_MESSAGE == signUpPage.personal_email_error()

    # This test will verify that when the user enters a password that
    # doesn't contain required pattern, an error message will appear
    @pytest.mark.parametrize(
        ("password_inputs", "error_message"),
        (
            (12345, SignUpPage.PASSWORD_NOT_MATCHING_CRITERIA_ERROR_MESSAGE),
            ("abc", SignUpPage.PASSWORD_NOT_MATCHING_CRITERIA_ERROR_MESSAGE),
            ("!@#", SignUpPage.PASSWORD_NOT_MATCHING_CRITERIA_ERROR_MESSAGE),
            ("1aA", SignUpPage.PASSWORD_NOT_MATCHING_CRITERIA_ERROR_MESSAGE),
            ("aA@", SignUpPage.PASSWORD_NOT_MATCHING_CRITERIA_ERROR_MESSAGE),
        )
    )
    def test_password_not_matching_criteria(self, password_inputs, error_message):
        signUpPage = SignUpPage()
        signUpPage.password_input().send_keys(password_inputs, Keys.RETURN)
        assert signUpPage.password_error_message().text == error_message
        try:
            assert bool(signUpPage.password_must_contain_tags())
        except NoSuchElementException as e:
            assert False, e

    # This test will verify that when the user enters a valid password,
    # the invalid password bar below the inputs  will not appear
    def test_password_that_matches_criteria(self):
        signUpPage = SignUpPage()
        signUpPage.password_input().send_keys(signUpPage.VALID_PASSWORD)
        try:
            x = signUpPage.password_must_contain_tags()
            assert False, "Invalid password bar shouldn't appear"
        except NoSuchElementException:
            assert True

    # This test will verify that when user clicks the login button, it will direct to the sign-in url
    def test_login_button(self):
        signUpPage = SignUpPage()
        signUpPage.login_button().click()
        time.sleep(1)
        assert driver.current_url == SIGN_IN_PAGE
