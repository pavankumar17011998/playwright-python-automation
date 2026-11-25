from playwright.sync_api import Page, Locator


class HomePage:
    """Page Object for the Playwright website."""

    # 1. Centralized URL: Change this once if the website URL changes
    URL = "https://playwright.dev/python"

    def __init__(self, page: Page):
        self.page = page

        # 2. Centralized Locators: Change this once if the link name/selector changes
        self.get_started_link: Locator = page.get_by_role("link", name="Get started")
        self.installation_heading: Locator = page.get_by_role("heading", name="Installation")

    def navigate(self) -> None:
        """Opens the home page URL."""
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def click_get_started(self) -> None:
        """Clicks the 'Get started' link."""
        self.get_started_link.click()
