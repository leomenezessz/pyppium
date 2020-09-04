import pytest
from assertpy import assert_that
from pyppium import driver
from pyppium.exception import CapabilitiesNoneException


@pytest.mark.unity
def test_should_get_driver_platform(mocker, mock_pyppium_instance, mock_desired_caps):
    spy = mocker.spy(driver, "platform_name")
    driver.platform_name()
    spy.assert_called_once_with()


@pytest.mark.unity
def test_should_verify_if_platform_is_android(
    mocker, mock_platform_name, mock_pyppium_instance
):
    mock_platform_name(mocker, "android")
    assert_that(driver.is_android()).is_true()


@pytest.mark.unity
def test_should_verify_if_platform_is_ios(
    mocker, mock_platform_name, mock_pyppium_instance
):
    mock_platform_name(mocker, "ios")
    assert_that(driver.is_ios()).is_true()


@pytest.mark.unity
def test_should_raise_exception_if_capabilities_is_none():
    with pytest.raises(CapabilitiesNoneException) as e:
        driver.PyppiumDriver(caps=None)
    assert_that(str(e.value)).is_equal_to("Capabilities cannot be None!")


@pytest.mark.unity
def test_should_connect_to_appium(mock_remote_connection):
    driver.PyppiumDriver(caps={})
    assert_that(driver.PyppiumDriver.instance()).is_not_none()


@pytest.mark.unity
def test_should_connect_to_browserstack(mock_remote_connection):
    driver.PyppiumDriver(caps={}, use_browserstack=True, user="", keys="")
    assert_that(driver.PyppiumDriver.instance()).is_not_none()


@pytest.mark.unity
def test_should_connect_to_browserstack(mock_remote_connection):
    driver.PyppiumDriver(caps={}, use_browserstack=True, user="", keys="")
    result = driver.PyppiumDriver.quit()
    assert_that(result).is_none()
