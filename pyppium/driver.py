from appium import webdriver
from pyppium import exception

_driver: webdriver.Remote


class PyppiumDriver(object):
    def __init__(
        self,
        caps,
        appium_url="http://localhost:4723/wd/hub",
        use_browserstack=False,
        **kwargs,
    ):

        global _driver

        if caps is None:
            raise exception.CapabilitiesNoneException("Capabilities cannot be None!")

        if "keys" in kwargs and "user" in kwargs and use_browserstack:
            _driver = webdriver.Remote(
                f"http://{kwargs['user']}:{kwargs['keys']}@hub-cloud.browserstack.com/wd/hub",
                caps,
            )
            return

        _driver = webdriver.Remote(appium_url, caps)

    @staticmethod
    def quit():
        if _driver is not None:
            _driver.quit()

    @staticmethod
    def instance() -> webdriver.Remote:
        return _driver


def platform_name():
    return PyppiumDriver.instance().desired_capabilities.get("platformName").lower()


def is_android():
    return platform_name() == "android"


def is_ios():
    return platform_name() == "ios"
