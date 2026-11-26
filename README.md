# Python Playwright Project

A clean, beginner-friendly Python web automation and testing project using [Playwright](https://playwright.dev/python/) and [pytest-playwright](https://playwright.dev/python/docs/intro).

---

## 📁 Project Structure

```text
project/
├── manual test cases/
│   └── Manual_Test_Cases.xlsx # Formatted Excel sheet mapping all test cases
├── pages/
│   ├── __init__.py
│   ├── base_page.py           # Base page with shared browser utilities
│   └── demo_page.py           # Demo app Page Object (URLs, locators, and actions)
├── tests/
│   ├── assets/
│   │   └── demo_app.html      # Self-contained testing application
│   ├── conftest.py            # Global test settings & browser configs
│   ├── test_forms.py          # UI & form interactions (inputs, dropdowns, checkboxes)
│   ├── test_validations.py    # Assertions, attributes, visibility, titles
│   ├── test_navigation.py     # Reloads, multi-tab popups
│   ├── test_dialogs.py        # JavaScript alerts and confirms
│   ├── test_mouse_keyboard.py # Hover tooltips and keyboard shortcuts
│   ├── test_files.py          # File upload and file download
│   ├── test_network.py        # Network interception and API mocking
│   └── test_responsive.py     # Mobile vs desktop viewports
├── .gitignore                 # Specifies files Git must ignore (.venv, cache, reports)
├── pytest.ini                 # Pytest configurations (default flags, test folders)
├── requirements.txt           # List of all project dependencies
└── README.md                  # Project documentation & guide
```

---

## ⚡ Quick Setup (After Downloading / Cloning from GitHub)

> [!TIP]
> Hover over any code block below and click the **Copy** button in the top-right corner to copy the command.

### All-in-One Setup (Run all at once in PowerShell)
```powershell
python -m venv .venv; .\.venv\Scripts\pip install -r requirements.txt; .\.venv\Scripts\playwright install chromium
```

---

### Step-by-Step Setup

#### Step 1: Create a virtual environment
```powershell
python -m venv .venv
```

#### Step 2: Install all required Python packages
```powershell
.\.venv\Scripts\pip install -r requirements.txt
```

#### Step 3: Install the Chromium browser binary
```powershell
.\.venv\Scripts\playwright install chromium
```

#### Step 4: Run the tests to confirm setup (Application Visible)
```powershell
.\.venv\Scripts\pytest --headed
```

---

## 📦 What is Installed in this Project? (Point-wise Breakdown)

1. **`playwright`**
   - The core browser automation library.
   - Automates modern web applications across Chromium, Chrome, Edge, Firefox, and WebKit.
   - Provides fast, reliable locators, auto-waiting, and network interception.

2. **`pytest`**
   - The standard Python test runner and framework.
   - Automatically discovers test files (`test_*.py`) and test functions (`test_*()`).
   - Generates test reports showing pass/fail status and failure stack traces.

3. **`pytest-playwright`**
   - The official plugin connecting Pytest and Playwright.
   - Injects the `page` fixture into test functions so you don't need to manually start/stop browser instances.
   - Provides CLI flags like `--headed`, `--browser`, `--slowmo`, `--tracing`, and automatic screenshot capture on failure.

4. **`pytest-html`**
   - Clean, lightweight HTML report generator.
   - Automatically generates a self-contained visual report (`reports/report.html`) after test runs.
   - No external servers, Java runtimes, or command-line binaries required.

5. **`python-dotenv`**
   - Allows loading configuration and credentials (like base URLs, usernames, passwords) from a `.env` file instead of hardcoding them in test scripts.

---

## ✍️ How to Write Test Code (Step-by-Step Guide)

All test files must be placed inside the `tests/` folder and must start with `test_` (e.g., `tests/test_login.py`).

### Step 1: Import `Page` and `expect`
Always import `Page` (for typing and autocomplete) and `expect` (for assertions):
```python
from playwright.sync_api import Page, expect
```

### Step 2: Define your test function
The function name must start with `test_` and accept `page: Page` as an argument:
```python
def test_user_login(page: Page):
```

### Step 3: Navigate to your URL
Use `page.goto()` to open the website:
```python
    page.goto("https://example.com/login")
```

### Step 4: Locate elements and interact
Playwright auto-waits for elements to be actionable before interacting with them:
- **Typing into inputs**:
```python
page.locator("#username").fill("my_username")
page.locator("#password").fill("my_password")
```
- **Clicking buttons or links**:
```python
page.get_by_role("button", name="Sign in").click()
```

### Step 5: Write assertions using `expect`
Assertions verify that the web page behaved as expected:
- **Check current URL**:
```python
expect(page).to_have_url("https://example.com/dashboard")
```
- **Check text or visibility**:
```python
expect(page.get_by_role("heading", name="Welcome")).to_be_visible()
```

---

### Complete Example (`tests/test_sample_login.py`)

Here is what a complete test looks like from start to finish:

```python
import re
from playwright.sync_api import Page, expect

def test_playwright_docs_search(page: Page):
    # 1. Navigate
    page.goto("https://playwright.dev/python")

    # 2. Assert page title
    expect(page).to_have_title(re.compile("Playwright"))

    # 3. Interact with an element
    page.get_by_role("link", name="Get started").click()

    # 4. Verify resulting page and elements
    expect(page).to_have_url(re.compile(".*intro"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
```

---

## 🏃 Running Commands Reference

Each command below is placed in its own block so you can copy it with one click:

#### Run all tests (runs in 4 parallel instances automatically)
```powershell
.\.venv\Scripts\pytest
```

#### Run tests with browser UI visible
```powershell
.\.venv\Scripts\pytest --headed
```

#### Run visible with 1-second delay between actions
```powershell
.\.venv\Scripts\pytest --headed --slowmo 1000
```

#### Run a specific test file
```powershell
.\.venv\Scripts\pytest tests/test_forms.py --headed
```

#### Run a specific test function by name
```powershell
.\.venv\Scripts\pytest -k "test_form_text_input" --headed
```

#### Auto-record user actions into Python code (Codegen)
```powershell
.\.venv\Scripts\playwright codegen https://playwright.dev
```

---

## 📊 Viewing the Test Report

Whenever you run `pytest`, a self-contained visual HTML report is automatically created in `reports/report.html` (no screenshots are stored, keeping the project light).

#### Open report in your default browser (Chrome/Edge):
```powershell
Start-Process reports/report.html
```
*(Or navigate to `reports/` in File Explorer and double-click `report.html`)*
