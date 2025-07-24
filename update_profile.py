import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Get credentials from GitHub Actions secrets
email = os.environ.get("NAUKRI_EMAIL")
password = os.environ.get("NAUKRI_PASS")

# Setup Chrome in headless mode for GitHub Actions
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    print("🔁 Opening Naukri login page...")
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    print("🔐 Entering login credentials...")
    driver.find_element(By.ID, "usernameField").send_keys(email)
    driver.find_element(By.ID, "passwordField").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)

    print("📂 Navigating to profile page...")
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    try:
        save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()
        print("✅ Profile updated successfully.")
    except NoSuchElementException:
        print("⚠️ Save button not found. Possibly already saved or page not loaded properly.")

except TimeoutException as e:
    print(f"❌ Timeout error occurred: {e}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
finally:
    print("🔚 Closing browser...")
    driver.quit()
