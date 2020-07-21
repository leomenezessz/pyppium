from assertpy import assert_that


def test_should_override_conf_with_user_settings(set_user_configuration, expected_user_configuration):
    from pyppium import settings
    assert_that(settings.config).is_equal_to(expected_user_configuration)


def test_should_use_default_conf(expected_default_config):
    from pyppium import settings
    assert_that(settings.config).is_equal_to(expected_default_config)
