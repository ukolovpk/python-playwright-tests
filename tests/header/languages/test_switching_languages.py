import pytest
from playwright.sync_api import Page, expect
from page_objects.pages.main.nodejs import MainNodeJsPage
from page_objects.pages.main.python import MainPythonPage


LANGUAGES = ["Python", "Java", ".NET"]


@pytest.mark.parametrize("language", LANGUAGES)
def test_switching_languages(page: Page, language):
    main_nodejs_page = MainNodeJsPage(page)
    main_nodejs_page.open()
    main_page = main_nodejs_page.header.choose_programming_language(language)
    expect(page).to_have_url(main_page.get_full_url())
    expect(main_page.header.brand_link).to_have_text(f"Playwright for {language}")


def test_switching_to_nodejs(page: Page):
    main_python_page = MainPythonPage(page)
    main_python_page.open()
    main_nodejs_page = main_python_page.header.choose_programming_language("Node.js")
    expect(page).to_have_url(main_nodejs_page.get_full_url())
    expect(main_nodejs_page.header.brand_link).to_have_text("Playwright")
