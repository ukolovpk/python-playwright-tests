import pytest
from playwright.sync_api import Page, expect
from page_objects.pages.main.python import MainPythonPage


@pytest.fixture(autouse=True)
def main_page(page: Page):
    page = MainPythonPage(page)
    page.open()
    return page


def test_saving_language_in_docs_path(page: Page, main_page):
    docs_page = main_page.header.click_to_docs()
    expect(page).to_have_url(docs_page.get_full_url())


def test_saving_language_in_api_path(page: Page, main_page):
    api_page = main_page.header.click_to_api()
    expect(page).to_have_url(api_page.get_full_url())


def test_saving_language_in_community_path(page: Page, main_page):
    community_page = main_page.header.click_to_community()
    expect(page).to_have_url(community_page.get_full_url())
