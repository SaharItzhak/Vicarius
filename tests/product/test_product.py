from tests.product.product_header import ProductHeader
from selenium.webdriver import ActionChains
from Pages.product_page import ProductPage
from conftest import driver
from constants import *
import pytest
import time


@pytest.mark.product
class TestProduct:
    """This group of tests are sanity tests for the product page"""

    # This test will verify that when user clicks the login button, it will direct to the sign-in url
    def test_login_button(self):
        productPage = ProductPage()
        productPage.login_button().click()
        time.sleep(1)
        assert driver.current_url == SIGN_IN_PAGE

    # This test will verify that when user clicks the start free trail button, it will direct to the sign-up url
    def test_start_free_trail_button(self):
        productPage = ProductPage()
        productPage.start_free_trail_button().click()
        time.sleep(1)
        assert driver.current_url == SIGN_UP_PAGE

    @pytest.mark.skip(reason="Fix mouse hover functionality")
    # This test will verify the dropdown when mouse hovers over the product button
    def test_mouse_hover_product(self):
        productPage = ProductPage()
        productHeader = ProductHeader()
        actions = ActionChains(driver)
        actions.move_to_element(productPage.product_button()).perform()

        assert productHeader.product_overview().is_enabled()
        assert productHeader.product_overview_description().is_enabled()

        assert productHeader.vulnerability_management().is_enabled()
        assert productHeader.vulnerability_management_description().is_enabled()

        assert productHeader.xTags().is_enabled()
        assert productHeader.xTags_descriptiom().is_enabled()

        assert productHeader.network_scanner().is_enabled()
        assert productHeader.network_scanner_description().is_enabled()

        assert productHeader.network_scanner().is_enabled()
        assert productHeader.network_scanner_description().is_enabled()

