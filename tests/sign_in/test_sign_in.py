from Pages.sign_in_page import SignInPage
from selenium.webdriver import Keys
from conftest import driver
from constants import *
import pytest
import time


@pytest.mark.sign_in
class TestSignIn:
    """This group of tests are sanity tests for the sign-in page"""

    # This test will verify a relevant error message when entering an invalid input to the email field
    @pytest.mark.parametrize(
        ("email_inputs", "invalid_email_message"),
        (
            (123, SignInPage.INVALID_EMAIL_MESSAGE),
            ("", SignInPage.INVALID_EMAIL_MESSAGE),
            ("namegmail.com", SignInPage.INVALID_EMAIL_MESSAGE),
            ("name@gmail", SignInPage.INVALID_EMAIL_MESSAGE),
            ("אבד@דהו", SignInPage.INVALID_EMAIL_MESSAGE)
        )
    )
    def test_invalid_email_input(self, email_inputs, invalid_email_message):
        signInPage = SignInPage()
        signInPage.email_input().send_keys(email_inputs, Keys.RETURN)
        assert signInPage.invalid_email_text() == invalid_email_message

    @pytest.mark.skip(reason="Separated into 2 different test cases")
    @pytest.mark.parametrize(
        ("email_inputs", "mail_not_found_message"),
        (
            (VALID_EMAIL_WITHOUT_ACCOUNT, SignInPage.INVALID_EMAIL_MESSAGE),
            (VALID_EMAIL_WITH_ACCOUNT, SignInPage.INVALID_EMAIL_MESSAGE),
        )
    )
    def test_valid_email_without_account(self, email_inputs, mail_not_found_message):
        signInPage = SignInPage()
        signInPage.email_input().send_keys(email_inputs, Keys.RETURN)
        assert signInPage.invalid_email_text() == mail_not_found_message

    # This test will the user will see the login page after a successful sign in with a valid account
    @pytest.mark.skip(reason="Waiting for a valid account")
    def test_email_with_account(self):
        signInPage = SignInPage()
        signInPage.email_input().send_keys(VALID_EMAIL_WITH_ACCOUNT, Keys.RETURN)
        pass
        # TODO - wait for email to be approved

    # This test will verify a relevant error message when entering a valid email
    # that doesn't have an active Vicarius account to the email field
    def test_email_without_account(self):
        signInPage = SignInPage()
        signInPage.email_input().send_keys(VALID_EMAIL_WITHOUT_ACCOUNT, Keys.RETURN)
        assert signInPage.invalid_email_error_message() == signInPage.EMAIL_NOT_FOUND_MESSAGE

    # This test will verify that when user clicks the start free trail button, it will direct to the sign-up url
    def test_start_free_trail_button(self):
        signInPage = SignInPage()
        signInPage.free_trail_button().click()
        time.sleep(1)
        assert driver.current_url == SIGN_UP_PAGE
