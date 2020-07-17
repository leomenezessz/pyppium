# Getting Started

This getting started is the most basic way to you start your tests with pyppium, the full documentation is under construction.

## Basic Usage

Above a basic sample of a screen with some elements to fetch called ScreenOne.

````python

# A Sample of a screen with different locators.

class ScreenOne:
    
    # fetch elements android and ios, by default pyppium wait element to be visible.

    _button = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))
    _text_field = fetch(iOS("id", "inputUserName"), Android("id", "username"))
    _text_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))

    # Login function with context elements.

    def login(self, username, password):
        self._text_field.send_keys(username)
        self._text_password.send_keys(password)
        self._button.click()
````

The ScreenTwo is another screen before login.

```python

class ScreenTwo:
    
    # fetching static label

    _label = fetch(iOS("id", "labelHello"), Android("id", "welcome_message"))
    
    # getting label text function

    def label_welcome_message(self):
        return self._label.text
```


Use page in your test case

```python

# A simple test simulate a login in a android app.

def test_android_basic_behaviours():
   
    # Test data

    username = "Lully"
    password = "123456789"

    # Capabilities to android

    caps_android ={
            "platformName": "Android",
            "automationName": "uiautomator2",
            "deviceName": "Android Emulator",
            "appPackage": "com.example.dummy",
            "appActivity": "MainActivity",
            "newCommandTimeout": 0,
    }
    
    # Start driver connection, with default url http://localhost:4723/wd/hub

    PyppiumDriver(caps_android)
    
    # Instantiate screen and call login function

    ScreenOne().login(username, password)
    
    # Assert the result in screen with assertpy

    assert_that(ScreenTwo().label_welcome_message()).contains(username)
    
    # Quit driver instance

    PyppiumDriver.quit()

```



