# Pyppium Driver

Pyppium driver is a abstraction to the conventional driver. He try to simplify driver usage and sharing instance in your test runner.

## Driver Basics

Pyppium driver have some facilities to use, and have some default parameters to simplify your tests. After start use pyppium remember to import it.

```python
from pyppium.driver import PyppiumDriver
```

### Connect to Appium Default Url 

If pyppium driver start only with caps he will connect to ```"http://localhost:4723/wd/hub"```.

```python

Pyppium(caps)

```

!!! Hint
    You can read more about appium capabilities in this [appium official documentation](http://appium.io/docs/en/writing-running-appium/caps/).

### Override Default Appium Url

You can override appium default url.

```python

Pyppium("http://my-domain/wd/hub", caps)

```

### Driver Instance

After create your driver instance you can access like that.

```python

Pyppium.instance()

```

This   `#!python instance()` call return a `#!python webdriver.Remote`. You can access atributes and functions as usual.

#### Screenshoot

```python
PyppiumDriver.instance().get_screenshot_as_png()
```

#### Checking Presence of Keyboard

```python
PyppiumDriver.instance().is_keyboard_shown()
```
#### Session

```python

# Return session

PyppiumDriver.instance().session

# Return session_id

PyppiumDriver.instance().session_id
```

!!! Note
    All these commands are from `#!python webdriver.Remote`, for more hot moves see [selenium official documentation](https://selenium-python.readthedocs.io/api.html).

## Getting Plataform Name

You can show the running plataform name simple like that.

```python

from pyppium import driver

# Will return the name of plataform in lower case.
# android or ios

driver.platform_name()

```

## Checking Running Platform

```python

from pyppium import driver

driver.is_android()

# Or 

driver.is_ios()


```

## Quitting Driver

Before kill driver instance pyppium only check if driver instance `#!python is not None`.


```python
PyppiumDriver.quit()
```

## PyppiumDriver and Browserstack

You can connect pyppium with browserstack like this.

````python
PyppiumDriver(caps, user="meiko", keys="keys", use_browserstack=True)
````

Change between local appium and browserstack is easy, just changing the flag `#!python False`.

````python
PyppiumDriver(caps, user="meiko", keys="keys", use_browserstack=False)
````

!!! Warning
    Remember browserstack have specific capabilities, you can check this in [browserstack official documentation](https://www.browserstack.com/app-automate/capabilities). 


## Pytest Real Life Sample

If you application have exactly the same behaviours you can run easy a test for android and ios with only one test.

First create you capabilities for android and ios.

```python

# Android appium capabilities

caps_android = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "Android Emulator",
    "appPackage": "com.example.dummy",
    "appActivity": "MainActivity",
    "newCommandTimeout": 0,
    "app": abspath("tests/e2e/apps/app-debug.apk")
}

# iOS appium capabilities

caps_ios = {
    "platformName": "iOS",
    "automationName": "xcuitest",
    "deviceName": "iPhone 8",
    "platformVersion": "13.6",
    "app": abspath("tests/e2e/apps/dummy.app")
}

```

Create your test case using parametrize and happy testing.

```python

@pytest.mark.parametrize("capabilities", [caps_ios, caps_android])
def test_should_show_welcome_message(capabilities):
    PyppiumDriver(capabilities)

    # You screens stuffs...

    PyppiumDriver.quit()

```

!!! Warning
    Remember create your screen using pyppium [fetcher]("https://leomenezessz.github.io/pyppium/fetcher/").






















