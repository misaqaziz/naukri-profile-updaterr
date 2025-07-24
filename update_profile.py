from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import traceback

print("🔁 Opening Naukri login page...")

# Chrome options for headless mode (for GitHub Actions)
options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Start browser
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.naukri.com/mnjuser/profile")

    print("🔐 Entering login credentials...")

    # Wait for the login form to load and enter email
    email_input = wait.until(EC.presence_of_element_located((By.ID, "usernameField")))
    email_input.send_keys(os.environ['NAUKRI_EMAIL'])

    # Enter password
    password_input = wait.until(EC.presence_of_element_located((By.ID, "passwordField")))
    password_input.send_keys(os.environ['NAUKRI_PASS'])

    # Click login
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "w60")))
    login_button.click()

    print("✅ Login submitted... waiting for profile to load.")

    # Wait for profile page or "Update" button to appear
    update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "update-text")))
    time.sleep(2)  # optional buffer
    update_button.click()

    print("📤 Profile updated!")

except Exception as e:
    print(f"❌ An error occurred: {e}")
    traceback.print_exc()

finally:
    print("🔚 Closing browser...")
    driver.quit()
