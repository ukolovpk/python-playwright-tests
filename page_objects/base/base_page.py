import os
from playwright.sync_api import Page


class BasePage:
    _MAIN_DOMAIN = os.getenv("PLAYWRIGHT_URL")
    _OTHER_DOMAIN = None

    def __init__(self, page: Page, path: str, url=None):
        self.page = page
        self._OTHER_DOMAIN = url
        self._path = path

    def open(self):
        self.page.goto(self.get_full_url())

    def get_full_url(self) -> str:
        print(self._OTHER_DOMAIN)
        return f"{self._OTHER_DOMAIN}{self._path}" if self._OTHER_DOMAIN else f"{self._MAIN_DOMAIN}{self._path}"

    def get_path(self) -> str:
        return self._path
