from pyppium.fetcher import fetch, iOS, Android


class ScreenOne:
    _button = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))
    _text_field = fetch(iOS("id", "inputUserName"), Android("id", "username"))
    _text_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))

    def login(self, username, password):
        self._text_field.send_keys(username)
        self._text_password.send_keys(password)
        self._button.click()


class ScreenTwo:
    _label = fetch(iOS("id", "labelHello"), Android("id", "welcome_message"))

    def label_welcome_message(self):
        return self._label.text
