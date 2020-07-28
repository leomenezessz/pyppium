# Decorators

The decorator's module has the objective to help in some common cross tests issues.
 
## Ignore Decorator

Let's check some common issue of the cross-testing when you don't have the same behaviours to the two platforms.

Thinking about two login screens in different platforms **(Android/iOS)** but that flow has the same result to the business because is the same product.

For **android** you have:  

 - A EditText for email 
 - A EditText for password
 - A Button for sign in
 - CheckBox before sign in


For **ios** you have:  

 - A EditText for email 
 - A EditText for password
 - A Button for sign in
 
Have a lot of ways to solve this problem, but the decorator `#!python ignore` try to do this whit some elegance.

````python

class LoginScreen:
    _button_sign_in = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))
    _input_username = fetch(iOS("id", "inputUserName"), Android("id", "username"))
    _input_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))
    _checkbox = fetch(android=Android("id", "checkbox"))

    @ignore(iOS.name)
    def click_checkbox(self):
        self._checkbox.click()

    def fill_email(self, email):
        self._input_username.send_keys(email)

    def fill_password(self, password):
        self._input_password.send_keys(password)

    def click_button_sign_in(self):
        self._button_sign_in.click()


````


With `#!python ignore` decorator you just need to send the platform name what you **want to ignore**.

When you run the tests to LoginScreen all tests should be pass because `#!python def click_checkbox() will not run for ios.

```python

@pytest.mark.parametrize("capabilities", [caps_ios, caps_android])
def test_login(capabilities, username, password):
    PyppiumDriver(capabilities)
    screen = LoginScreen()
    screen.fill_email(username)
    screen.fill_password(password)
    screen.click_checkbox()
    screen.click_button_sign_in()
    assert username in ScreenTwo().label_welcome_message()

```

<br/>

    
