import json
from playwright.sync_api import Page, Route, expect
from pages.demo_page import DemoAppPage


def test_mock_api_success_response(page: Page):
    """Example 1: Intercepting network call and returning mocked JSON response."""
    # Intercept https://api.example.com/users and return custom mock data
    def handle_route(route: Route):
        mock_data = {"user": "Alice Wonder"}
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mock_data)
        )

    page.route("https://api.example.com/users", handle_route)

    demo_page = DemoAppPage(page)
    demo_page.load()

    # Click button that triggers fetch
    demo_page.fetch_users_button.click()

    # Assert mocked user name appears in UI
    expect(demo_page.api_user_name).to_have_text("Alice Wonder")


def test_mock_api_server_error(page: Page):
    """Example 2: Simulating server error (500) and asserting failure handling."""
    # Intercept https://api.example.com/users and fulfill with 500 server error
    page.route("https://api.example.com/users", lambda route: route.fulfill(status=500, body="Server Error"))

    demo_page = DemoAppPage(page)
    demo_page.load()

    # Click button to trigger fetch
    demo_page.fetch_users_button.click()

    # Assert UI displays fallback 'Fetch Failed' text
    expect(demo_page.api_user_name).to_have_text("Fetch Failed")
