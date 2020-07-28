from pyppium.fetcher import fetch, iOS, Android


class LoginScreen:
    _button_sign_in = fetch(iOS("id", "buttonSignIn"), Android("id", "button"))
    _input_username = fetch(iOS("id", "inputUserName"), Android("id", "username"))
    _input_password = fetch(iOS("id", "InputPassword"), Android("id", "pass"))

    def fill_email(self, email):
        self._input_username.send_keys(email)

    def fill_password(self, password):
        self._input_password.send_keys(password)

    def click_button_sign_in(self):
        self._button_sign_in.click()


class WelcomeScreen:
    _label = fetch(iOS("id", "labelHello"), Android("id", "welcome_message"))

    def label_welcome_message(self):
        return self._label.text
