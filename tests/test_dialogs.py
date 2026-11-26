from playwright.sync_api import Page, expect
from pages.demo_page import DemoAppPage


def test_javascript_alert_dialog(page: Page):
    """Example 1: Triggering JavaScript alert and asserting dialog message."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Handle dialog event
    def handle_alert(dialog):
        assert dialog.type == "alert"
        assert dialog.message == "Hello from Playwright alert!"
        dialog.accept()

    page.on("dialog", handle_alert)

    # Click button that triggers alert
    demo_page.alert_button.click()


def test_javascript_confirm_dialog(page: Page):
    """Example 2: Accepting confirm dialog and asserting result text."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Accept the confirm dialog
    page.on("dialog", lambda dialog: dialog.accept())

    # Click confirm button
    demo_page.confirm_button.click()

    # Assert result text in DOM updated to 'Confirmed'
    expect(demo_page.dialog_result).to_have_text("Confirmed")
