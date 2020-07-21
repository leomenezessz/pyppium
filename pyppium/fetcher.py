from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from pyppium import condition, exception, driver
from pyppium.settings import config

_SELENIUM_LOCATORS = None
_APPIUM_LOCATORS = None
_FETCH_TIMEOUT = config["driver"]["timeout"]


def _validate_fetch(locator, plat):
    if (
        locator not in _get_appium_locators()
        and locator not in _get_selenium_locators()
    ):
        raise exception.InvalidLocatorException(
            f"Invalid locator '{locator}' to {plat} platform."
        )


def _get_selenium_locators():
    global _SELENIUM_LOCATORS
    if _SELENIUM_LOCATORS is None:
        _SELENIUM_LOCATORS = list(vars(By).values())
    return _SELENIUM_LOCATORS


def _get_appium_locators():
    global _APPIUM_LOCATORS
    if _APPIUM_LOCATORS is None:
        _APPIUM_LOCATORS = list(vars(MobileBy).values())
    return _APPIUM_LOCATORS


class iOS:
    name = "ios"

    def __init__(self, by, value):
        _validate_fetch(by, self.name)
        self.by = by
        self.value = value


class Android:
    name = "android"

    def __init__(self, by, value):
        _validate_fetch(by, self.name)
        self.by = by
        self.value = value


class fetch(object):
    def __init__(
        self,
        ios: iOS = None,
        android: Android = None,
        timeout=_FETCH_TIMEOUT,
        wait_condition="default",
    ):

        self._timeout = timeout
        self._ios = ios
        self._android = android
        self._wait_condition = getattr(
            condition, wait_condition, condition.wait_visibility_of_element
        )

    def __get__(self, instance, owner) -> WebElement:

        if driver.is_android():
            return self._wait_condition(
                self._android.by, self._android.value, self._timeout
            )
        elif driver.is_ios():
            return self._wait_condition(self._ios.by, self._ios.value, self._timeout)
        else:
            raise exception.InvalidPlatformException("Invalid Platform!")


class fetches(object):
    def __init__(
        self,
        ios: iOS = None,
        android: Android = None,
        timeout=_FETCH_TIMEOUT,
        wait_condition="default",
    ):
        self.timeout = timeout
        self.ios = ios
        self.android = android
        self.wait_condition = getattr(
            condition, wait_condition, condition.wait_visibility_of_elements
        )

    def __get__(self, instance, owner):
        if driver.is_android():
            return self.wait_condition(
                self.android.by, self.android.value, self.timeout
            )
        elif driver.is_ios():
            return self.wait_condition(self.ios.by, self.ios.value, self.timeout)
        else:
            raise exception.InvalidPlatformException("Invalid Platform!")
