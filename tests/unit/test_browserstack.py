import pytest
from assertpy import assert_that
from pyppium.browserstack import BrowserStackApi


@pytest.mark.vcr
def test_show_recent_uploads():
    resp = BrowserStackApi().recent_uploads()
    assert_that(resp.status_code).is_equal_to(200)
    assert_that(resp.json()).is_instance_of(list)
    assert_that(resp.json()[0]).contains_key(
        "app_name", "app_version", "app_url", "app_id", "uploaded_at"
    )


@pytest.mark.vcr
def test_delete_app():
    resp = BrowserStackApi().delete_app("8cda444d6390db17b0a144be79be9ed996406dbc")
    assert_that(resp.status_code).is_equal_to(200)
    assert_that(resp.json()).is_equal_to({"success": True})


@pytest.mark.vcr
def test_get_apps_by_custom_id():
    resp = BrowserStackApi().get_apps_by_custom_id("android")
    assert_that(resp.status_code).is_equal_to(200)
    assert_that(resp.json()).is_instance_of(list)
    assert_that(resp.json()[0]).contains_key(
        "app_name",
        "app_version",
        "app_url",
        "app_id",
        "uploaded_at",
        "custom_id",
        "shareable_id",
    )


@pytest.mark.vcr
@pytest.mark.parametrize(
    "upload",
    [
        {
            "custom_id": "android",
            "expected": {
                "app_url": "bs://8cda444d6390db17b0a144be79be9ed996406dbc",
                "custom_id": "android",
                "shareable_id": "pyppium-user/android",
            },
        },
        {
            "custom_id": None,
            "expected": {"app_url": "bs://355e6259172efcdd09c49bae90d7f464e8ca2036"},
        },
    ],
)
def test_upload_app(
    upload, mock_open_file, mock_httpx_content_stream_headers, mock_httpx_encode
):
    resp = BrowserStackApi().upload_app("path/to/my/app", upload["custom_id"])
    assert_that(resp.status_code).is_equal_to(200)
    assert_that(resp.json()).is_equal_to(upload["expected"])


@pytest.mark.vcr
def test_update_browserstack_test_status(expected_upload_test_response):
    resp = BrowserStackApi().update_test_status(
        "f3069db4f92225471e4926e28563a08f63a48674",
        "passed",
        "No reason, its just a test!",
    )
    assert_that(resp.status_code).is_equal_to(200)
    assert_that(resp.json()).is_equal_to(expected_upload_test_response)
