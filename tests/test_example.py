import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    """Test that the Playwright Python home page contains the expected title."""
    page.goto("https://playwright.dev/python")

    # Expect page title to contain substring
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    """Test navigating to the installation guide via Get started link."""
    page.goto("https://playwright.dev/python")

    # Click the 'Get started' link
    page.get_by_role("link", name="Get started").click()

    # Expect the URL to contain 'intro'
    expect(page).to_have_url(re.compile(".*intro"))

    # Expect the heading 'Installation' to be visible
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
