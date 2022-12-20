from page_objects.base.base_page import BasePage
from playwright.sync_api import Page
from page_objects.fragments.header import Header


class MainNodeJsPage(BasePage):
    def __init__(self, page: Page, url="/"):
        super().__init__(page, url)
        self._header_container = self.page.locator(".navbar")
        self.header = Header(page, self._header_container)
