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


@pytest.fixture
def logged_in_context(context: BrowserContext):
    """Example fixture for pre-configuring authentication or cookies if needed."""
    # Custom cookies/storage state can be set here:
    # context.add_cookies([...])
    yield context
