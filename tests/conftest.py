import pytest
from playwright.sync_api import BrowserContext, Page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Override default browser context arguments (e.g. viewport, permissions, timezone)."""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        },
        "ignore_https_errors": True,
    }


@pytest.fixture(autouse=True)
def configure_timeouts(page: Page):
    """Fail fast: Do NOT wait 30 seconds. Fail in 10 seconds if a page or element hangs."""
    page.set_default_navigation_timeout(10000)  # 10s max for page.goto()
    page.set_default_timeout(10000)             # 3s max for click(), fill(), etc.
    yield
