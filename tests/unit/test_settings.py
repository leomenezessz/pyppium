import pytest
from assertpy import assert_that
from pyppium import exception


def test_should_override_conf_with_user_settings(set_user_configuration, expected_user_configuration):
    from pyppium import settings
    assert_that(settings.config).is_equal_to(expected_user_configuration)


def test_should_use_default_conf(expected_default_config):
    from pyppium import settings
    assert_that(settings.config).is_equal_to(expected_default_config)


def test_should_raise_exception_for_invalid_yaml(set_wrong_yaml_configuration):
    with pytest.raises(exception.InvalidSettingsException):
        from pyppium import settings
        assert_that(settings.config)
