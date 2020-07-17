from typing import List
from selenium.webdriver.remote.webelement import WebElement
from pyppium.exception import NotFoundElementToClickException


def elements_list_to_string_list(elements: List[WebElement]):
    string_list = []
    for element in elements:
        string_list.append(element.text)
    return string_list


def click_in_element_list_by_text(element_list: List[WebElement], text):
    for element in element_list:
        if element.text == text:
            element.click()
            return
    raise NotFoundElementToClickException(
        f"Element with the text {text} could not be found in the list."
    )


def click_in_element_list_if_contains_text(element_list: List[WebElement], text):
    for element in element_list:
        if text in element.text:
            element.click()
            return
    raise NotFoundElementToClickException(
        f"No one element with the text {text} can be found in the list."
    )
