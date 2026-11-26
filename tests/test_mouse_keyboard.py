from playwright.sync_api import Page, expect
from pages.demo_page import DemoAppPage


def test_mouse_hover_reveals_tooltip(page: Page):
    """Example 1: Hovering over an element and asserting tooltip visibility."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Hover over target element
    demo_page.hover_target.hover()

    # Assert tooltip is now displayed
    expect(demo_page.hover_tooltip).to_be_visible()


def test_keyboard_actions_and_shortcuts(page: Page):
    """Example 2: Typing text, selecting all with Control+A, and clearing with Backspace."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Focus and type into input
    demo_page.username_input.focus()
    demo_page.username_input.press_sequentially("SampleText")
    expect(demo_page.username_input).to_have_value("SampleText")

    # Select all and delete using keyboard shortcuts
    demo_page.username_input.press("Control+A")
    demo_page.username_input.press("Backspace")

    # Assert input is now empty
    expect(demo_page.username_input).to_have_value("")
