import inspect
import json
import sys
from httpx import Response
from loguru import logger


def _request_success(resp: Response, backtrace):
    logger.remove()

    logger.add(
        sys.stderr,
        format="\n<level>{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}</>",
        level="SUCCESS",
        colorize=True,
    )

    logger.success(
        f"{backtrace} :\n"
        f"URL ==> {resp.url}\n"
        f"STATUS ==> {resp.status_code}\n"
        f"BODY ==> {json.dumps(resp.json(), indent=4)}"
    )


def _request_error(resp: Response, backtrace):
    logger.remove()

    logger.add(
        sys.stderr,
        format="\n<level>{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}</>",
        level="ERROR",
        colorize=True,
    )

    logger.error(
        f"{backtrace} :\n"
        f"URL ==> {resp.url}\n"
        f"STATUS ==> {resp.status_code}\n"
        f"HEADERS ==> {resp.headers.items()}"
    )


class response(object):
    def __call__(self, function):
        def wrapper(*args, **kwargs):
            module = (
                args[0].__module__
                if "self" in inspect.getfullargspec(function).args
                else self.__module__
            )
            backtrace = f"{module}.{function.__name__}"

            resp = function(*args, **kwargs)

            if resp.status_code != 200:
                _request_error(resp, backtrace)
            else:
                _request_success(resp, backtrace)

            return resp

        return wrapper
