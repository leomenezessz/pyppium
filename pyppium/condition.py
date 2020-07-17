from typing import List
from appium.webdriver import WebElement
from selenium.webdriver.support import wait, expected_conditions as expect
from pyppium.driver import PyppiumDriver

VISIBILITY = "wait_visibility_of_element"
VISIBILITIES = "wait_visibility_of_elements"
VISIBILITY_OF_ANYS = "wait_visibility_of_any_elements"
PRESENCE = "wait_presence_of_element"


def wait_visibility_of_element(by, value, timeout) -> WebElement:
    return wait.WebDriverWait(PyppiumDriver.instance(), timeout).until(
        expect.visibility_of_element_located((by, value))
    )


def wait_visibility_of_elements(by, value, timeout) -> List[WebElement]:
    return wait.WebDriverWait(PyppiumDriver.instance(), timeout).until(
        expect.visibility_of_all_elements_located((by, value))
    )


def wait_visibility_of_any_elements(by, value, timeout) -> List[WebElement]:
    return wait.WebDriverWait(PyppiumDriver.instance(), timeout).until(
        expect.visibility_of_any_elements_located((by, value))
    )


def wait_presence_of_element(by, value, timeout) -> WebElement:
    return wait.WebDriverWait(PyppiumDriver.instance(), timeout).until(
        expect.presence_of_element_located((by, value))
    )
