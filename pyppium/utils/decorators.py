from pyppium import driver


class ignore(object):
    def __init__(self, platform):
        self._platform = platform

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            if self._platform == driver.platform_name():
                return
            return function(*args, **kwargs)

        return wrapper
