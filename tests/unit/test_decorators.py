import pytest
from assertpy import assert_that
from pyppium.utils.decorators import ignore


@pytest.mark.unity
@pytest.mark.parametrize("platform", ["android", "ios"])
def test_should_not_run_function_if_ignore_platform(mocker, platform):
    mocker.patch("pyppium.driver.platform_name", return_value=platform)

    @ignore(platform)
    def dumb_function():
        return "Pyppium!"

    assert_that(dumb_function()).is_equal_to(None)


@pytest.mark.unity
@pytest.mark.parametrize("platform", ["android", "ios"])
def test_should_run_function_if_not_ignore_platform(mocker, platform):
    mocker.patch("pyppium.driver.platform_name", return_value="windows-phone")

    @ignore(platform)
    def dumb_function():
        return "Pyppium!"

    assert_that(dumb_function()).is_equal_to("Pyppium!")
