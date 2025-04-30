# BookCart Test Cases and Automation Test

This project contains test cases and an automated smoke test that verifies the login functionality of the BookCart (https://bookcart.azurewebsites.net) web application using Selenium and Python.

## Smoke Test 

**Test Objective**:  
Verify that a user can successfully log in using a valid, pre-existing account.

**Test Data**:
- **Username**: `testuser11`
- **Password**: `Test1234`

**Target URL**:  
https://bookcart.azurewebsites.net/login

---

### Prerequisites

- Python 3.8+
- Google Chrome (latest version)
- Pip package manager

> This project uses Selenium Manager (included in Selenium 4.6+) so no manual ChromeDriver setup is needed.

---

### Installation

1. **Clone this repository**
    ```bash
    git clone https://github.com/farahzip/bookcart-tests.git
    cd bookcart-tests

2. Install dependencies
    ```bash
    pip install -r requirements.txt

3. Run the Test File
    ```bash
    bookcart-tests/smoke test.py

4.  Expected Output
    ```bash
    Login test passed.
If the login fails or elements are not found, a traceback will be printed.
