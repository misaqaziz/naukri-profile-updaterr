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
chrome_options.add_argument("--window-size=1920,1080")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    print("🔁 Opening Naukri login page...")
    driver.get("https://www.naukri.com/mnjuser/login")
    time.sleep(4)

    print("🔐 Entering login credentials...")
    driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(5)

    print("📂 Navigating to profile page...")
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    print("📝 Editing headline to trigger update...")
    try:
        edit_btn = driver.find_element(By.XPATH, '//span[text()="Edit"]')
        edit_btn.click()
        time.sleep(2)

        headline_input = driver.find_element(By.XPATH, '//textarea[@name="headline"]')
        old_text = headline_input.get_attribute("value")
        new_text = old_text.strip() + " ."
        headline_input.clear()
        headline_input.send_keys(new_text)

        save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
        save_button.click()
        print("✅ Profile headline updated successfully.")

    except NoSuchElementException:
        print("⚠️ Edit or Save button not found. Possibly already updated or page not loaded properly.")

except TimeoutException as e:
    print(f"❌ Timeout error occurred: {e}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
finally:
    print("🔚 Closing browser...")
    driver.quit()
