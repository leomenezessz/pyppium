import os
from os.path import abspath
from typing import List
import appium
import pytest
from appium.webdriver import WebElement
from assertpy import add_extension


@pytest.fixture
def android_caps():
    return {
        "platformName": "Android",
        "automationName": "uiautomator2",
        "deviceName": "Android Emulator",
        "appPackage": "com.example.dummy",
        "appActivity": "MainActivity",
        "newCommandTimeout": 0,
        "app": abspath("tests/e2e/apps/app-debug.apk"),
    }


def is_all_items_instance_of(self, instance):
    for item in self.val:
        if not isinstance(item, instance):
            self.error(f"This value: {item} is NOT instance of {instance}")
        return self


@pytest.fixture(scope="module")
def items_isinstance_extension():
    add_extension(is_all_items_instance_of)


@pytest.fixture
def ios_caps():
    return {
        "platformName": "iOS",
        "automationName": "xcuitest",
        "deviceName": "iPhone 8",
        "platformVersion": "13.3",
        "app": abspath("tests/e2e/apps/dummy.app"),
    }


@pytest.fixture
def username():
    return "PyUser"


@pytest.fixture
def password():
    return "123456789"


@pytest.fixture
def mock_selenium_wait(mocker):
    mocker.patch(
        "selenium.webdriver.support.wait.WebDriverWait.until", return_value=WebElement
    )


@pytest.fixture
def mock_pyppium_instance(mocker):
    mocker.patch(
        "pyppium.driver.PyppiumDriver.instance", return_value=appium.webdriver.Remote
    )


@pytest.fixture
def mock_selenium_waits(mocker):
    mocker.patch(
        "selenium.webdriver.support.wait.WebDriverWait.until",
        return_value=List[WebElement],
    )


@pytest.fixture
def mock_selenium_click(mocker):
    mocker.patch(
        "selenium.webdriver.remote.webelement.WebElement.click", return_value=None
    )


@pytest.fixture
def mock_list_of_web_elements():
    return web_element_list


@pytest.fixture
def mock_web_element_text():
    return web_element_text


def web_element_text(mocker, text):
    mocker.patch("selenium.webdriver.remote.webelement.WebElement.text", text)


def web_element_list(mocker):
    mock = mocker.MagicMock()
    mock.__iter__.return_value = [WebElement, WebElement]
    return mock


@pytest.fixture
def expected_selenium_locators():
    return [
        "id",
        "xpath",
        "link text",
        "partial link text",
        "name",
        "tag name",
        "class name",
        "css selector",
    ]


@pytest.fixture
def expected_appium_locators():
    return [
        "-ios predicate string",
        "-ios uiautomation",
        "-ios class chain",
        "-android uiautomator",
        "-android viewtag",
        "-android datamatcher",
        "-android viewmatcher",
        "-windows uiautomation",
        "accessibility id",
        "-image",
        "-custom",
    ]


@pytest.fixture
def mock_platform():
    return set_platform


def set_platform(mocker, android: bool, ios: bool):
    mocker.patch("pyppium.driver.is_android", return_value=android)
    mocker.patch("pyppium.driver.is_ios", return_value=ios)


@pytest.fixture
def mock_desired_caps(mocker):
    mocker.patch("appium.webdriver.Remote.desired_capabilities")


@pytest.fixture
def mock_platform_name():
    return platform_name


def platform_name(mocker, name):
    mocker.patch("pyppium.driver.platform_name", return_value=name)


@pytest.fixture
def mock_remote_connection(mocker):
    mocker.patch("appium.webdriver.Remote")


@pytest.fixture
def expected_user_configuration():
    return {
        "driver": {
            "timeout": 45,
            "appium_url": "http://localhost:3333/wd/hub",
            "browserstack_url": "@hub-cloud.browserstack.com/wd/hub:8080",
        }
    }


@pytest.fixture
def expected_default_config():
    return {
        "driver": {
            "timeout": 15,
            "appium_url": "http://localhost:4723/wd/hub",
            "browserstack_url": "@hub-cloud.browserstack.com/wd/hub",
        }
    }


@pytest.fixture
def set_user_configuration(request, expected_user_configuration):
    config = """
            # Pyppium simple yaml config.
    
            driver:
              timeout: 45
              appium_url: "http://localhost:3333/wd/hub"
              browserstack_url: "@hub-cloud.browserstack.com/wd/hub:8080"
          
            """

    root_dir = abspath("./pyppium.yaml")

    with open(root_dir, "x") as file:
        file.write(config)

    def delete_yaml_file():
        os.remove(root_dir)

    request.addfinalizer(delete_yaml_file)
