from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")

    # Login
    driver.find_element(By.ID, "usernameField").send_keys("your-email@example.com")
    driver.find_element(By.ID, "passwordField").send_keys("your-password")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)  # wait for login to complete

    # Navigate to profile
    driver.get("https://www.naukri.com/mnjuser/profile")

    time.sleep(5)

    # Simulate update — click "Edit" on summary or something similar
    # For example: update resume headline or save button
    try:
        save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()
        print("Profile updated successfully!")
    except:
        print("Could not locate update button, but login likely worked.")

finally:
    driver.quit()
