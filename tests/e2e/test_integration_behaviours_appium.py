import pytest
from assertpy import assert_that
from pyppium.driver import PyppiumDriver
from tests.e2e.screens.screen import ScreenOne, ScreenTwo


@pytest.mark.regression
def test_android_basic_behaviours(android_caps, username, password):
    PyppiumDriver(android_caps)
    ScreenOne().login(username, password)
    assert_that(ScreenTwo().label_welcome_message()).contains(username)


@pytest.mark.regression
def test_ios_basic_behaviours(ios_caps, username, password):
    PyppiumDriver(ios_caps)
    ScreenOne().login(username, password)
    assert_that(ScreenTwo().label_welcome_message()).contains(username)
