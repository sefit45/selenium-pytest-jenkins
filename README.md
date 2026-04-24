# Selenium Pytest Jenkins Automation Framework

## Overview

This project is a complete end-to-end QA Automation Framework designed for enterprise-level test automation using Python, Selenium WebDriver, Pytest, Jenkins CI/CD, GitHub integration, Allure Reports, HTML Reports, API Testing, and Database Validation.

The framework covers UI automation, API automation, authentication flows, database validation, reporting, and continuous integration workflows commonly used in large-scale production environments.

---

## Key Features

### UI Automation

* Selenium WebDriver with Python
* Page Object Model (POM) architecture
* Reusable fixtures using `conftest.py`
* Login validation scenarios
* Navigation flow validation
* Screenshot capture on failure
* Regression and smoke test support

### API Automation

* REST API testing using Python Requests
* GET / POST validation
* Authentication and token handling
* Negative testing scenarios
* Full API chaining (Login → Token → Protected API)
* Response validation and JSON assertions

### Database Validation

* SQL validation using SQLite
* Backend data verification
* Insert / Select validation
* End-to-end API → Database verification

### Reporting

* HTML Reports using `pytest-html`
* Allure Reports for enterprise-grade reporting
* Failure screenshots embedded in reports
* Full execution visibility and defect analysis

### CI/CD Integration

* Jenkins integration
* GitHub repository integration
* Scheduled execution support
* Automated regression execution
* Continuous testing workflow

---

## Project Structure

```text
PythonProjects/
│
├── Pages/
│   ├── login_page.py
│   └── wikipedia_page.py
│
├── Tests/
│   ├── test_login.py
│   ├── test_wikipedia.py
│   ├── test_api.py
│   ├── test_auth_api.py
│   ├── test_auth_chain_api.py
│   ├── test_negative_auth.py
│   ├── test_database.py
│   └── test_full_e2e_flow.py
│
├── screenshots/
├── allure-results/
├── report.html
├── customers.db
├── conftest.py
└── requirements.txt