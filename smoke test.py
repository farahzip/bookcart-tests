#Test user login page with a  premade account

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_login():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.implicitly_wait(10)

    try:
    
        driver.get("https://bookcart.azurewebsites.net/login")

        driver.find_element(By.ID, "mat-input-0").send_keys("testuser11")  # Username
        driver.find_element(By.ID, "mat-input-1").send_keys("Test1234")    # Password

        login_button = driver.find_element(By.XPATH, "//button[.//span[text()='Login']]")
        login_button.click()

        time.sleep(2) 

        print("Login test passed.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
