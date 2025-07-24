# naukri_update.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Read credentials from environment variables
EMAIL = os.environ["NAUKRI_EMAIL"]
PASSWORD = os.environ["NAUKRI_PASSWORD"]

# Setup headless Chrome (invisible browser)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start Chrome
driver = webdriver.Chrome(options=options)

def update_profile():
    try:
        print("Opening Naukri...")
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(5)

        print("Logging in...")
        driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
        driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(7)

        print("Trying to simulate profile update...")
        driver.find_element(By.XPATH, "//span[contains(text(),'Edit')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()

        print("✅ Profile updated successfully!")

    except Exception as e:
        print("❌ Error during update:", e)
    finally:
        driver.quit()

update_profile()
