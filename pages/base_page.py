from pathlib import Path
from playwright.sync_api import Page, Locator


class BasePage:
    """Base Page Object containing shared browser actions and common utilities."""

    def __init__(self, page: Page):
        self.page = page

    def get_title(self) -> str:
        """Returns the current page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Returns the current page URL."""
        return self.page.url

    def reload_page(self) -> None:
        """Reloads the current page."""
        self.page.reload()
