from Pages.product_page import ProductPage
from selenium.webdriver.common.by import By
from conftest import driver


class ProductHeader(ProductPage):
    """This class is a children class of the product page and will represent the dropdown menu of the product button"""

    def product_overview(self):
        return driver.find_element(By.LINK_TEXT, "Product Overview")

    def product_overview_description(self):
        return driver.find_element(By.XPATH, "Product Overview")

    def vulnerability_management(self):
        return driver.find_element(By.LINK_TEXT, "Vulnerability Management")

    def vulnerability_management_description(self):
        return driver.find_element(By.LINK_TEXT, "Discover, prioritize, and remediate vulnerabilities "
                                                 "all from a single, intuitive platform.")

    def xTags(self):
        return driver.find_element(By.LINK_TEXT, "xTags")

    def xTags_descriptiom(self):
        return driver.find_element(By.LINK_TEXT, "Internal and external threat prioritization by contextual factors")

    def network_scanner(self):
        return driver.find_element(By.LINK_TEXT, "Network Scanner")

    def network_scanner_description(self):
        return driver.find_element(By.LINK_TEXT, "Get full visibility into your network, visualized "
                                                 "in an intuitive vulnerability scanning dashboard")

    def patch_management(self):
        return driver.find_element(By.LINK_TEXT, "Patch Management")

    def patch_management_description(self):
        return driver.find_element(By.LINK_TEXT, "Remediate vulnerabilities quicker with our "
                                                 "advanced, integral patch management tools")

    def patchless_protection(self):
        return driver.find_element(By.LINK_TEXT, "Patchless Protection")

    def patchless_protection_description(self):
        return driver.find_element(By.LINK_TEXT, "Beat the patch gap and stay protected "
                                                 "with or without a security patch.")
