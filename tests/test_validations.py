from playwright.sync_api import Page, expect
from pages.demo_page import DemoAppPage


def test_element_visibility_and_page_title(page: Page):
    """Example 1: Asserting element visibility, enabled status, and page title."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Assert page title
    expect(page).to_have_title("Playwright Automation Sandbox")

    # Assert submit button is visible and enabled
    expect(demo_page.submit_button).to_be_visible()
    expect(demo_page.submit_button).to_be_enabled()


def test_element_attributes_and_placeholder(page: Page):
    """Example 2: Asserting input placeholder, attribute values, and element count."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Assert placeholder attribute of username input
    expect(demo_page.username_input).to_have_attribute("placeholder", "Enter username")

    # Assert number of country options (1 default + 3 countries = 4)
    options = demo_page.country_select.locator("option")
    expect(options).to_have_count(4)
