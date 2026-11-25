import re
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_has_title(page: Page):
    """Test that the Playwright Python home page contains the expected title."""
    home_page = HomePage(page)
    home_page.navigate()

    # Expect page title to contain substring
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    """Test navigating to the installation guide via Get started link."""
    home_page = HomePage(page)
    home_page.navigate()

    # Click the 'Get started' link via Page Object
    home_page.click_get_started()

    # Expect the URL to contain 'intro'
    expect(page).to_have_url(re.compile(".*intro"))

    # Expect the heading 'Installation' to be visible
    expect(home_page.installation_heading).to_be_visible()
