import os
from os.path import abspath
import yaml
from pyppium.exception import InvalidSettingsException

PYPPIUM_CONFIG_PATH = abspath("pyppium.yaml")

config = {
    "driver": {
        "timeout": 15,
        "appium_url": "http://localhost:4723/wd/hub",
        "browserstack_url": "@hub-cloud.browserstack.com/wd/hub",
    }
}


if os.path.exists(PYPPIUM_CONFIG_PATH):
    with open(PYPPIUM_CONFIG_PATH, "r") as stream:
        try:
            user_conf = yaml.safe_load(stream)
            if user_conf is not None and "driver" in config:
                config["driver"].update(user_conf["driver"])
        except Exception as error:
            raise InvalidSettingsException(error)
