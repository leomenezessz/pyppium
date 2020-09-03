import json
from os import environ, path
import httpx
from httpx import Response
from loguru import logger


class BrowserStackApi:
    _BASE_URL = "https://api-cloud.browserstack.com/app-automate"
    _DELETE_APP = f"{_BASE_URL}/app/delete/"
    _RECENT_APPS = f"{_BASE_URL}/recent_apps/"
    _UPLOAD = f"{_BASE_URL}/upload"
    _SESSION = f"{_BASE_URL}/sessions/"

    def __init__(self, user=None, password=None):
        self.user = environ["BROWSERSTACK_USERNAME"] if user is None else user
        self.password = environ["BROWSERSTACK_ACCESS_KEY"] if password is None else password

    def upload_app(self, app_path, custom_id=None):
        full_app_path = path.abspath(app_path)
        data = json.dumps({"custom_id": custom_id})

        files = {
            "file": (full_app_path, open(full_app_path, "rb")),
            "data": (None, data),
        }

        httpx.post(
            self._BASE_URL + self._UPLOAD,
            files=files,
            auth=(self.user, self.password),
            timeout=None,
        )

    def recent_uploads(self):
        logger.info("DISPATCHING REQUEST {}", self._RECENT_APPS)

        response = httpx.get(self._RECENT_APPS, auth=(self.user, self.password))

    def delete_app(self, app_id):
        httpx.delete(
            self._BASE_URL + self._DELETE_APP + app_id, auth=(self.user, self.password)
        )

    def get_apps_by_custom_id(self, custom_id):
        httpx.get(
            self._BASE_URL + self._RECENT_APPS + custom_id,
            auth=(self.user, self.password),
        )

    def update_test_status(self, session, result):
        data = {"status": result, "reason": ""}

        httpx.put(
            f"{self._BASE_URL}{self._SESSION}{session}.json",
            auth=(self.user, self.password),
            data=data,
        )


def reponse_log(response: Response) -> Response:
    if response.status_code != 200:
        logger.error(
            f"URL ==> {response.url}\n"
            f"STATUS ==> {response.status_code}\n"
            f"HEADERS ==> {json.dumps(response.headers.items(), indent=4)}"
        )
    else:
        logger.info(
            f"RESPONSE START =================>\n"
            f"URL ==> {response.url}\n"
            f"STATUS ==> {response.status_code}\n"
            f"BODY ==> {json.dumps(response.json(), indent=4)}"
            f"\nRESPONSE END ====================>\n"
        )

    return response
