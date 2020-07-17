from typing import List
import pytest
from appium.webdriver import WebElement
from assertpy import assert_that
from pyppium import fetcher
from pyppium.exception import InvalidPlatformException, InvalidLocator
from pyppium.fetcher import Android, iOS


@pytest.mark.unity
def test_should_get_selenium_locators(expected_selenium_locators):
    locators = fetcher._get_selenium_locators()
    assert_that(locators).is_instance_of(list)
    assert_that(expected_selenium_locators).is_subset_of(locators)


@pytest.mark.unity
def test_should_get_appium_locators(expected_appium_locators):
    locators = fetcher._get_appium_locators()
    assert_that(locators).is_instance_of(list)
    assert_that(expected_appium_locators).is_subset_of(locators)


@pytest.mark.unity
@pytest.mark.parametrize("platform", ["android", "ios"])
def test_should_validate_fetch(mocker, platform):
    spy = mocker.spy(fetcher, "_validate_fetch")
    fetcher._validate_fetch("id", platform)
    spy.assert_called_once_with("id", platform)


@pytest.mark.unity
@pytest.mark.parametrize(
    "platform", [{"android": True, "ios": False}, {"android": False, "ios": True}]
)
def test_should_fetch_element_by_platform(
    mocker,
    mock_platform,
    mock_pyppium_instance,
    mock_selenium_wait,
    mock_selenium_click,
    platform,
):
    mock_platform(mocker, platform["android"], platform["ios"])

    class Screen:
        element = fetcher.fetch(iOS("id", "test"), Android("id", "test"))

    click_result = Screen().element.click()
    assert_that(click_result).is_none()


@pytest.mark.unity
@pytest.mark.parametrize(
    "platform", [{"android": True, "ios": False}, {"android": False, "ios": True}]
)
def test_should_fetches_elements_by_plataform(
    mocker,
    mock_platform,
    mock_pyppium_instance,
    mock_selenium_waits,
    mock_selenium_click,
    platform,
):
    mock_platform(mocker, platform["android"], platform["ios"])

    class Screen:
        elements = fetcher.fetches(iOS("id", "test"), Android("id", "test"))

    assert_that(Screen().elements).is_instance_of(List[WebElement].__class__)


@pytest.mark.unity
def test_should_raise_exception_to_invalid_platform_in_fetch(
    mocker,
    mock_selenium_wait,
    mock_pyppium_instance,
    mock_platform,
    mock_selenium_click,
):
    mock_platform(mocker, android=False, ios=False)

    class Screen:
        element = fetcher.fetch(iOS("id", "test"), Android("id", "test"))

    with pytest.raises(InvalidPlatformException) as e:
        Screen().element.click()
    assert_that(str(e.value)).is_equal_to("Invalid Platform!")


@pytest.mark.unity
def test_should_raise_exception_to_invalid_platform_in_fetches(
    mocker,
    mock_selenium_waits,
    mock_pyppium_instance,
    mock_platform,
    mock_selenium_click,
):
    mock_platform(mocker, android=False, ios=False)

    class Screen:
        elements = fetcher.fetches(iOS("id", "test"), Android("id", "test"))

    with pytest.raises(InvalidPlatformException) as e:
        element_one = Screen().elements[0]
    assert_that(str(e.value)).is_equal_to("Invalid Platform!")


@pytest.mark.unity
@pytest.mark.parametrize("platform", ["android", "ios"])
def test_should_raise_exception_to_invalid_locator(platform):
    wrong_locator = "ID"
    with pytest.raises(InvalidLocator) as e:
        fetcher._validate_fetch(wrong_locator, platform)
    assert_that(str(e.value)).is_equal_to(
        f"Invalid locator '{wrong_locator}' to {platform} platform."
    )
