from playwright.sync_api import Page, expect
from pages.demo_page import DemoAppPage


def test_page_reload_and_url_assertion(page: Page):
    """Example 1: Navigating, reloading the page, and asserting URL persistence."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Reload page
    demo_page.reload_page()

    # Assert that current URL contains the demo app file name
    expect(page).to_have_url(demo_page.PAGE_URL.as_uri())


def test_multi_tab_popup_handling(page: Page):
    """Example 2: Clicking link that opens a new tab, asserting popup creation."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Expect popup when clicking link with target="_blank"
    with page.expect_popup() as popup_info:
        demo_page.new_tab_link.click()

    new_tab = popup_info.value
    new_tab.wait_for_load_state("domcontentloaded")

    # Assert new tab page was created and has expected domain
    assert "playwright.dev" in new_tab.url
    new_tab.close()
