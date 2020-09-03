from pyppium.browserstack import BrowserStackApi


def test_show_recent_uploads():
    BrowserStackApi().recent_uploads()
