from page_objects.pages.main.nodejs import MainNodeJsPage
from playwright.sync_api import Page


class MainDotNetPage(MainNodeJsPage):
    def __init__(self, page: Page):
        super().__init__(page, "/dotnet/")
