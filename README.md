# Pyppium

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![codecov](https://codecov.io/gh/leomenezessz/pyppium/branch/master/graph/badge.svg)](https://codecov.io/gh/leomenezessz/pyppium)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/leomenezessz/pyppium/blob/master/LICENSE)
![GitHub Pages Deploy](https://github.com/leomenezessz/pyppium/workflows/GitHub%20Pages%20Deploy/badge.svg?branch=master)

Pyppium is a Appium-Python-Client wrapper for cross mobile testing. 
It provides a simple and concise way to build your tests, saving your time and focusing on what really matters in your (Android/iOS) Application. 


## Installation

```

$ pip install pyppium

```

## Basic Usage

The following code will give you the necessary to create a simple flow that searches for components on your application screen and perform an action.
Others components are supported based on the Appium usage, so feel free to explore and setup your own custom actions.

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

After that, you can use the class above (ScreenOne) to create an specific scenario. 
Note that you need to start Pyppium Driver.

```python

from pyppium.driver import PyppiumDriver
from tests.e2e.screens.screen import ScreenOne, ScreenTwo


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

    assert username in ScreenTwo().label_welcome_message()

    PyppiumDriver.quit()
```

## Documentation

- https://leomenezessz.github.io/pyppium/

## Special Thanks
 
 Pyppium count on many packages for trying to deliver a good framework. And of course, these packages are amazing!
 
 - [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/)
 - [PyYAML](https://pypi.org/project/PyYAML/)
 - [Pytest](https://pypi.org/project/pytest/)
 - [Assertpy](https://pypi.org/project/assertpy/)
 - [Black](https://pypi.org/project/black/)
 - [Pytest-mock](https://pypi.org/project/pytest-mock/)
 - [Pytest-cov](https://pypi.org/project/pytest-cov/)
 - [Codecov](https://pypi.org/project/codecov/)
 - [Mkdocs](https://pypi.org/project/mkdocs/)
 - [Tox](https://pypi.org/project/tox/) 
 - [Mkdocs-material](https://squidfunk.github.io/mkdocs-material/) 

## License

 The MIT License (MIT)
 Copyright (c) 2020 Leonardo Menezes

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
 OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
 OR OTHER DEALINGS IN THE SOFTWARE.
 
 <br/>