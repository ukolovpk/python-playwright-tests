from page_objects.base.base_page import BasePage
from playwright.sync_api import Page


class ApiPage(BasePage):
    def __init__(self, page: Page, path=None, url=None):
        self._path = path if path else "docs/api/class-playwright"
        super().__init__(page, self._path, url)
