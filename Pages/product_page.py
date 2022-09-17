from selenium.webdriver.common.by import By
from conftest import driver
from constants import *
import pytest


@pytest.mark.usefixtures("setup_teardown")
class ProductPage:
    def __init__(self):
        driver.get(PRODUCT_PAGE)

    def login_button(self):
        return driver.find_element(By.LINK_TEXT, "Login")

    def start_free_trail_button(self):
        return driver.find_element(By.LINK_TEXT, "Start Free Trial")

    def product_button(self):
        return driver.find_elements(By.XPATH, "//button[@class='link']")[0]

    def solution_button(self):
        return driver.find_elements(By.XPATH, "//button[@class='link']")[1]

    def pricing_button(self):
        return driver.find_elements(By.XPATH, "//button[@class='link']")[2]

    def community_button(self):
        return driver.find_elements(By.XPATH, "//button[@class='link']")[3]

    def company_button(self):
        return driver.find_elements(By.XPATH, "//button[@class='link']")[4]

    def contact_button(self):
        return driver.find_elements(By.XPATH, "//button[@class='link']")[5]
