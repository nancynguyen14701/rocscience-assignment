# Rocscience Take-home Assignment

Automated tests covering desktop, web, and API testing.

## Project Structure

```
.
├── task1_desktop/
│   ├── output                 # Contains Notepad created files
│   ├── config.py              # Test configuration constants
│   ├── pages/
│   │   └── notepad_page.py    # Page Object for Notepad (pywinauto)
│   ├── tests/
│   │   ├── conftest.py        # Test fixtures
│   │   └── test_notepad.py    # Desktop automation tests
│   └── utils/
│       ├── file_helper.py     # File operations
│       └── waits.py           # Window/file polling helpers
│
├── task2_web/
│   ├── conftest.py            # Browser fixtures (Playwright)
│   ├── pages/
│   │   ├── base_page.py       # Base Page Object
│   │   ├── home_page.py       # Home page interactions
│   │   └── login_page.py      # Login page interactions
│   └── tests/
│       └── test_login.py      # Login flow tests
│
├── task2b_api/
│   ├── README.md
│   └── test_invalid_login.py  # API login validation
│
├── requirements.txt
└── README.md
```

## Prerequisites

- **Python 3.9+**
- **Windows 11** (for desktop Notepad automation)
- Screen must not be locked during desktop tests

## Setup

```bash
# Create and activate Python virtual environment
cd rocscience-assignment
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate.bat   # Windows CMD
.venv\Scripts\Activate.ps1   # Windows Powershell

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers (for web tests)
playwright install
```

## Running the Tests

### Desktop Automation (Notepad)

```bash
pytest task1_desktop/ -v
```

Uses **pywinauto** with UI Automation backend to control Notepad by element
properties (control type, automation ID) — no coordinates.

### Web Automation (Login Tests)

```bash
pytest task2_web/ -v
```

Uses **Playwright** with Page Object Model to test login flows on
`https://rocscience.com`:
- Navigate to home page
- Access login portal
- Verify login form elements

### API Automation

```bash
pytest task2b_api/ -v
# or
python task2b_api/test_invalid_login.py
```

Tests login via HTTP POST using `requests`:
- Invalid credentials (expects rejection 400 Bad request)

## Design Decisions

- **Desktop**: Uses **pywinauto** UIA backend — locates controls by `control_type` and `auto_id` instead of screen coordinates
- **Web**: Page Object Model separates locators from test logic. Uses **Playwright** for modern browser automation
- **API**: Simple `requests` calls with redirect inspection

## Dependencies

| Package | Purpose |
|---------|---------|
| `pywinauto` | Desktop UI automation |
| `playwright` | Browser automation |
| `requests` | HTTP client for API tests |
| `pytest` | Test framework |
