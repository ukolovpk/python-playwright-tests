from playwright.sync_api import Page, Locator
from page_objects.base.base_fragment import BaseFragment
from page_objects.base.elements.dropdown import Dropdown


class Header(BaseFragment):
    def __init__(self, page: Page, parent_locator: Locator):
        super().__init__(page, parent_locator)

        self.navbar_items_left = self.parent.locator(".navbar__items")
        self.brand_link = self.navbar_items_left.locator("[class*=brand]")
        self.docs_link = self.navbar_items_left.locator("text=Docs")
        self.api_link = self.navbar_items_left.locator("text=API")
        self.language_dropdown = Dropdown(page, self.navbar_items_left.locator(".dropdown"))
        self.community_link = self.navbar_items_left.locator("text=Community")

        self.navbar_items_right = self.parent.locator("[class*=right]")
        self.github_link = self.navbar_items_right.locator("[class*=github-link]")
        self.color_mode_toggle = self.navbar_items_right.locator("[class*=colorModeToggle]")
        self.search_box = self.navbar_items_right.locator("[class*=searchBox]")

    def click_to_logo(self):
        from page_objects.pages.main.nodejs import MainNodeJsPage
        url = self.page.url
        self.brand_link.click()
        return MainNodeJsPage(self.page, url=url)

    def click_to_docs(self):
        from page_objects.pages.docs.docs_page import DocsPage
        url = self.page.url
        self.docs_link.click()
        return DocsPage(self.page, url=url)

    def click_to_api(self):
        from page_objects.pages.api.api_page import ApiPage
        url = self.page.url
        self.api_link.click()
        return ApiPage(self.page, url=url)

    def _programming_language_hover(self):
        self.language_dropdown.parent.hover()

    def choose_programming_language(self, language: str):
        from page_objects.pages.main.nodejs import MainNodeJsPage
        from page_objects.pages.main.python import MainPythonPage
        from page_objects.pages.main.java import MainJavaPage
        from page_objects.pages.main.dot_net import MainDotNetPage
        pages = {
            "Node.js": MainNodeJsPage(self.page),
            "Python": MainPythonPage(self.page),
            "Java": MainJavaPage(self.page),
            ".NET": MainDotNetPage(self.page),
        }
        self._programming_language_hover()
        self.language_dropdown.choose_option(language)
        try:
            return pages[language]
        except ValueError as e:
            return e

    def click_to_community(self):
        from page_objects.pages.community.community_page import CommunityPage
        url = self.page.url
        self.community_link.click()
        return CommunityPage(self.page, url=url)
