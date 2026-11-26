from playwright.sync_api import Page, expect
from pages.demo_page import DemoAppPage


def test_desktop_viewport_layout(page: Page):
    """Example 1: Desktop viewport (1280x720) - Desktop nav visible, mobile menu hidden."""
    page.set_viewport_size({"width": 1280, "height": 720})

    demo_page = DemoAppPage(page)
    demo_page.load()

    # Assert desktop navbar is visible and mobile hamburger is hidden
    expect(demo_page.desktop_nav).to_be_visible()
    expect(demo_page.mobile_hamburger).to_be_hidden()


def test_mobile_viewport_layout(page: Page):
    """Example 2: Mobile viewport (375x667) - Mobile hamburger visible, desktop nav hidden."""
    page.set_viewport_size({"width": 375, "height": 667})

    demo_page = DemoAppPage(page)
    demo_page.load()

    # Assert mobile hamburger is visible and desktop navbar is hidden
    expect(demo_page.mobile_hamburger).to_be_visible()
    expect(demo_page.desktop_nav).to_be_hidden()
