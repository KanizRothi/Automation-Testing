# Beginner UI Automation Testing Project

**Project:** Demo E-commerce Website UI Automation  
**Tools:** Python, Selenium, pytest  
**Website under test:** https://www.saucedemo.com/

## Goal
Practice beginner-level UI automation: login, error validation, product listing, and cart workflows.

> Learning project for the public demo site only. Do not use it on real websites/accounts without permission.

## Setup

Prerequisites: Python 3.10+, Google Chrome, and internet access.

Create a virtual environment:

**Linux/macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Selenium Manager usually finds a compatible browser driver automatically.

## Run the tests

```bash
pytest -v
```

Run one test:
```bash
pytest tests/test_saucedemo.py::test_login_with_valid_credentials
```

Save a JUnit XML report:
```bash
pytest --junitxml=reports/junit-report.xml
```

Optional HTML report:
```bash
pip install pytest-html
pytest --html=reports/report.html --self-contained-html
```

## Included test cases

| ID | Scenario | Expected result |
|---|---|---|
| TC-01 | Login with valid demo credentials | Products page appears |
| TC-02 | Login with an invalid password | Error message appears |
| TC-03 | Product listing | One or more product cards appear |
| TC-04 | Add a product to cart | Cart badge shows 1 |
| TC-05 | Open cart | Added product appears |

Demo credentials commonly provided by SauceDemo: `standard_user` / `secret_sauce`. Confirm them on the website if the demo changes.

## GitHub checklist
- Run the tests yourself and fix failures.
- Include only reports and screenshots you actually generated.
- Keep real credentials and secrets out of GitHub.
- Be ready to explain the locators, assertions, fixtures, and test cases in an interview.

## CV description (only after completing and understanding the project)

**Beginner UI Automation Testing Project | Selenium, Python, pytest**
- Created automated UI tests for login, product listing, and cart workflows on a public demo e-commerce website.
- Used pytest assertions to validate page behavior and error messages.
- Organized browser setup and cleanup using pytest fixtures.
- Generated a test execution report using pytest (include only if you actually generated one).
