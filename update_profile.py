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
    driver.get("https://www.naukri.com/nlogin/login")

    print("🔐 Entering login credentials...")

    # Wait and input credentials
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys(os.environ['NAUKRI_EMAIL'])

    password_input = wait.until(EC.presence_of_element_located((By.NAME, "PASSWORD")))
    password_input.send_keys(os.environ['NAUKRI_PASS'])

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login_button.click()

    print("✅ Login submitted... waiting for profile to load.")

    # Wait for profile update button
    wait.until(EC.url_contains("profile"))  # wait until redirected
    time.sleep(3)  # wait extra to be safe

    update_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "update-text")))
    update_button.click()

    print("📤 Profile updated!")

except Exception as e:
    print(f"❌ An error occurred: {e}")
    traceback.print_exc()

finally:
    print("🔚 Closing browser...")
    driver.quit()
