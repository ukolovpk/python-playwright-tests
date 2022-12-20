from page_objects.base.base_fragment import BaseFragment
from playwright.sync_api import Page, Locator


class Dropdown(BaseFragment):
    def __init__(self, page: Page, parent_locator: Locator):
        super().__init__(page, parent_locator)

    def choose_option(self, option_text: str):
        self.parent.locator("[data-language-prefix]").filter(has_text=option_text).click()
