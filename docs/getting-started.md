# QuickStart

The fastest way to start using pyppium is learning the about basic pyppium driver and fetcher.

## Basic Usage of Pyppium Driver

Create your capabilities as usual.

```python

caps_android = {

            "platformName": "Android",
            "automationName": "uiautomator2",
            "deviceName": "Android Emulator",
            "appPackage": "com.example.dummy",
            "appActivity": "MainActivity",
            "newCommandTimeout": 0,
}

```

Import and add capabilities in pyppium driver init.

```python

from pyppium.driver import PyppiumDriver

PyppiumDriver(caps_android)

```

Quit driver after test run.

```python
    
PyppiumDriver.quit()

```

!!! Info
    The pyppium driver default url connects to **```http://localhost:4723/wd/hub```**,
    if you want to override send url parameter like this sample **``` 
    PyppiumDriver("http://my-url-here", caps_android)```**
    

## Basic Usage of Fetcher

Structure your screen with fetcher, this sample is about a login screen.


````python

from pyppium.fetcher import fetch, iOS, Android


class ScreenOne:
    

    _button = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))
    _text_field = fetch(iOS("id", "inputUserName"), Android("id", "username"))
    _text_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))


    def login(self, username, password):
        self._text_field.send_keys(username)
        self._text_password.send_keys(password)
        self._button.click()

````

In this app the another screen is a welcome screen before login.

```python

from pyppium.fetcher import fetch, iOS, Android


class ScreenTwo:
    
    _label = fetch(iOS("id", "labelHello"), Android("id", "welcome_message"))
    
    def label_welcome_message(self):
        return self._label.text

```

!!! Info
    The fetcher always wait element to be visible.

## Testing

Create your test and use your screens and pyppium driver.

```python

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

!!! warning
    The fetcher module search element by platform in capabilities. 
    He only search for **Android** or **iOS**, if **```platformName```** is 
    android he looking for android element and if ios he looking for
    ios element.

<br/>




