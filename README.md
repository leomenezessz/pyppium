# Pyppium

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![codecov](https://codecov.io/gh/leomenezessz/pyppium/branch/master/graph/badge.svg)](https://codecov.io/gh/leomenezessz/pyppium)
[![Documentation Status](https://readthedocs.org/projects/pyppium/badge/?version=latest)](https://pyppium.readthedocs.io/en/latest/?badge=latest)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/leomenezessz/pyppium/blob/master/LICENSE)



Pyppium is a wrapper of Appium-Python-Client for cross mobile testing.

## Installation

```
$ pip install pyppium
```

## Basic Usage

Create your screen like this

```python
from pyppium.fetcher import fetch, iOS, Android


class ScreenOne:
    _button = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))
    _text_field = fetch(iOS("id", "inputUserName"), Android("id", "username"))
    _text_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))

    def login(self, username, password):
        self._text_field.send_keys(username)
        self._text_password.send_keys(password)
        self._button.click()

    
```

User your screen in test after start pyppium driver

```python
from pyppium.driver import PyppiumDriver
from tests.e2e.screens.screen import ScreenOne, ScreenTwo
from assertpy import assert_that


def test_android_basic_behaviours():
    username = "Lully"
    password = "123456789"

    caps_android ={
            "platformName": "Android",
            "automationName": "uiautomator2",
            "deviceName": "Android Emulator",
            "appPackage": "com.example.dummy",
            "appActivity": "MainActivity",
            "newCommandTimeout": 0,
    }


    PyppiumDriver(caps_android)
    ScreenOne().login(username, password)
    assert_that(ScreenTwo().label_welcome_message()).contains(username)
    PyppiumDriver.quit()
```

## Documentation

- https://pyppium.readthedocs.io/en/latest/








