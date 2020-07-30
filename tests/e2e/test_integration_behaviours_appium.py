from os.path import abspath
import pytest
from assertpy import assert_that
from pyppium.driver import PyppiumDriver
from tests.e2e.screens.screen import LoginScreen, WelcomeScreen

caps_android = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "Android Emulator",
    "appPackage": "com.example.dummy",
    "appActivity": "MainActivity",
    "newCommandTimeout": 0,
    "app": abspath("tests/e2e/apps/app-debug.apk"),
}

caps_ios = {
    "platformName": "iOS",
    "automationName": "xcuitest",
    "deviceName": "iPhone 8",
    "platformVersion": "13.3",
    "app": abspath("tests/e2e/apps/dummy.app"),
}


@pytest.mark.regression
@pytest.mark.parametrize("capabilities", [caps_android, caps_ios])
def test_android_basic_behaviours(capabilities, username, password):
    PyppiumDriver(capabilities)
    screen = LoginScreen()
    screen.fill_email(username)
    screen.fill_password(password)
    screen.click_button_sign_in()
    assert_that(WelcomeScreen().label_welcome_message()).contains(username)


