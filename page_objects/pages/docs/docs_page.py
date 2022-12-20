from page_objects.base.base_page import BasePage
from playwright.sync_api import Page


class DocsPage(BasePage):
    def __init__(self, page: Page, path=None, url=None):
        self._path = path if path else "docs/intro"
        super().__init__(page, self._path, url)
