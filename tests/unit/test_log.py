import pytest
from assertpy import assert_that
from pyppium import log


@pytest.mark.unity
def test_log_request_success(success_response, mocker):
    mocked_request_success = mocker.patch("pyppium.log._request_success")
    mocked_request_success(success_response, __name__)
    mocked_request_success.assert_called_with(success_response, __name__)


@pytest.mark.unity
def test_log_request_error(mocker, failure_response):
    mocked_request_error = mocker.patch("pyppium.log._request_error")
    mocked_request_error(failure_response, __name__)
    mocked_request_error.assert_called_with(failure_response, __name__)


@pytest.mark.unity
def test_log_response_decorator_function_without_params(success_response):
    @log.response()
    def dumb_function():
        return success_response

    assert_that(dumb_function().json()).is_equal_to(success_response.json())


@pytest.mark.unity
def test_log_response_decorator_function_with_params(success_response):
    @log.response()
    def dumb_function(s):
        print(s)
        return success_response

    assert_that(dumb_function("").json()).is_equal_to(success_response.json())


@pytest.mark.unity
def test_log_response_decorator_with_a_function_class(success_response):
    class Test:
        @log.response()
        def dumb_function(self):
            return success_response

    assert_that(Test().dumb_function().json()).is_equal_to(success_response.json())


@pytest.mark.unity
def test_log_response_decorator_with_a_function_class_request_error(failure_response):
    class Test:
        @log.response()
        def dumb_function(self):
            return failure_response

    assert_that(Test().dumb_function()).is_equal_to(failure_response)
