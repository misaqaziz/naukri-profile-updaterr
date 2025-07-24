import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

email = os.environ.get("NAUKRI_EMAIL")
password = os.environ.get("NAUKRI_PASS")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)
    driver.find_element(By.ID, "usernameField").send_keys(email)
    driver.find_element(By.ID, "passwordField").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    try:
        save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()
        print("✅ Profile updated successfully.")
    except:
        print("⚠️ Save button not found, login may have worked though.")

finally:
    driver.quit()
