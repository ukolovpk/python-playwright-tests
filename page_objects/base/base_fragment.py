from playwright.sync_api import Page, Locator
from lib.shared.timeouts import Timeouts


class BaseFragment:
    def __init__(self, page: Page, parent_locator: Locator = None):
        self.page = page
        self.parent = parent_locator if parent_locator else self.page.locator("body")
        self._timeout = Timeouts.default_gui_timeout
