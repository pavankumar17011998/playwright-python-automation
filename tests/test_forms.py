from playwright.sync_api import Page, expect
from pages.demo_page import DemoAppPage


def test_form_text_input_and_submission(page: Page):
    """Example 1: Typing text into input, submitting form, and asserting output."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Fill username and submit
    demo_page.fill_and_submit_form("JohnDoe")

    # Assert that confirmation message appears with the entered username
    expect(demo_page.form_result).to_have_text("Welcome, JohnDoe!")


def test_dropdown_and_checkbox_selection(page: Page):
    """Example 2: Selecting dropdown option, checking checkbox, and asserting states."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Select country and check terms
    demo_page.select_country_and_agree_terms("IN")

    # Assert dropdown selected value and checkbox checked state
    expect(demo_page.country_select).to_have_value("IN")
    expect(demo_page.terms_checkbox).to_be_checked()
