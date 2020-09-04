import json
from os import environ, path
import httpx
from pyppium import log


class BrowserStackApi:
    _BASE_URL = "https://api-cloud.browserstack.com/app-automate"
    _DELETE_APP = f"{_BASE_URL}/app/delete/"
    _RECENT_APPS = f"{_BASE_URL}/recent_apps/"
    _UPLOAD = f"{_BASE_URL}/upload"
    _SESSION = f"{_BASE_URL}/sessions/"

    def __init__(self, user=None, password=None):
        self.user = environ["BROWSERSTACK_USERNAME"] if user is None else user
        self.password = (
            environ["BROWSERSTACK_ACCESS_KEY"] if password is None else password
        )

    @log.response()
    def upload_app(self, app_path, custom_id=None):
        full_app_path = path.abspath(app_path)
        data = json.dumps({"custom_id": custom_id})

        files = {
            "file": (full_app_path, open(full_app_path, "rb")),
            "data": (None, data),
        }

        return httpx.post(
            self._UPLOAD,
            files=files,
            auth=(self.user, self.password),
            timeout=None,
        )

    @log.response()
    def recent_uploads(self):
        return httpx.get(self._RECENT_APPS, auth=(self.user, self.password))

    @log.response()
    def delete_app(self, app_id):
        return httpx.delete(
            f"{self._DELETE_APP}{app_id}",
            auth=(self.user, self.password),
        )

    @log.response()
    def get_apps_by_custom_id(self, custom_id):
        return httpx.get(
            f"{self._RECENT_APPS}{custom_id}",
            auth=(self.user, self.password),
        )

    @log.response()
    def update_test_status(self, session, result, reason=""):
        data = {"status": result, "reason": reason}

        return httpx.put(
            f"{self._SESSION}{session}.json", auth=(self.user, self.password), data=data
        )
