from selenium.common import NoSuchElementException


def is_element_displayed(element):
    try:
        return bool(element)
    except NoSuchElementException as e:
        print(e)
        return False
