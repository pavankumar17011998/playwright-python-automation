from pathlib import Path
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class DemoAppPage(BasePage):
    """Page Object for the Demo Application.
    Centralizes all element locators and page actions so changes happen in one place.
    """

    # Resolve local HTML file path as a file:// URL
    PAGE_URL = Path(__file__).resolve().parent.parent / "tests" / "assets" / "demo_app.html"

    def __init__(self, page: Page):
        super().__init__(page)

        # --- Navigation Locators ---
        self.desktop_nav: Locator = page.locator("#desktop-nav")
        self.mobile_hamburger: Locator = page.locator("#mobile-hamburger")
        self.new_tab_link: Locator = page.locator("#open-new-tab")

        # --- Form Locators ---
        self.username_input: Locator = page.locator("#username")
        self.country_select: Locator = page.locator("#country")
        self.terms_checkbox: Locator = page.locator("#terms")
        self.submit_button: Locator = page.locator("#submit-btn")
        self.form_result: Locator = page.locator("#form-result")

        # --- Interactions & Dialogs Locators ---
        self.hover_target: Locator = page.locator("#hover-target")
        self.hover_tooltip: Locator = page.locator("#hover-tooltip")
        self.alert_button: Locator = page.locator("#alert-btn")
        self.confirm_button: Locator = page.locator("#confirm-btn")
        self.dialog_result: Locator = page.locator("#dialog-result")

        # --- File Locators ---
        self.file_uploader: Locator = page.locator("#file-uploader")
        self.upload_status: Locator = page.locator("#upload-status")
        self.download_link: Locator = page.locator("#download-link")

        # --- Network / API Locators ---
        self.fetch_users_button: Locator = page.locator("#fetch-users-btn")
        self.api_user_name: Locator = page.locator("#api-user-name")

    def load(self) -> None:
        """Navigates to the local demo application."""
        self.page.goto(self.PAGE_URL.as_uri())

    def fill_and_submit_form(self, username: str) -> None:
        """Fills the username input and clicks the submit button."""
        self.username_input.fill(username)
        self.submit_button.click()

    def select_country_and_agree_terms(self, country_code: str) -> None:
        """Selects country from dropdown and checks terms checkbox."""
        self.country_select.select_option(country_code)
        self.terms_checkbox.check()
