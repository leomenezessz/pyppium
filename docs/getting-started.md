# QuickStart

The fastest way to start using pyppium is to learn about the basics: Pyppium's fetcher and PyppiumDriver.

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

Import PyppiumDriver and pass the capababilities to `PyppiumDriver`'s initializer

```python

from pyppium.driver import PyppiumDriver

PyppiumDriver(caps_android)

```

Call driver's `quit` method after running the tests.

```python
    
PyppiumDriver.quit()

```

!!! Info
    PyppiumDriver's default url connects to **```http://localhost:4723/wd/hub```**,
    May you wish to override it, pass an URL parameter before the capabilities, as follows: **``` 
    PyppiumDriver("http://my-url-here", caps_android)```**
    

## Basic Usage of Fetcher

Structure your screen with fetcher, this sample covers a login screen.


````python

from pyppium.fetcher import fetch, iOS, Android


class ScreenOne:
    

    _button_sign_in = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))
    _input_username = fetch(iOS("id", "inputUserName"), Android("id", "username"))
    _input_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))


    def login(self, username, password):
        self._input_username.send_keys(username)
        self._input_password.send_keys(password)
        self._button_sign_in.click()

````

The screen below is a welcome screen, presented before login.

```python

from pyppium.fetcher import fetch, iOS, Android


class ScreenTwo:
    
    _label_welcome_message = fetch(iOS("id", "labelHello"), Android("id", "welcome_message"))
    
    def label_welcome_message(self):
        return self._label_welcome_message.text

```

!!! Info
    The fetcher always awaits for elements to become visible.

## Testing

Create your test and use your screens and PyppiumDriver.

```python

def test_android_basic_behaviours():
   
    username = "lully"
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
    The fetcher module searches elements in capabilities by the platform. 
    It only searches for **Android** or **iOS**, so if **```platformName```** is
    `android`, it's looking for the Android element and if it's `ios`, it's looking for
    the iOS element.

<br/>




