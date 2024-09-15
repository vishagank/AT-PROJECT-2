from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the webdriver
driver = webdriver.Chrome()

# 1. Launch the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# 2. Login as Admin
# Wait for username field and enter "Admin"
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# Wait for password field and enter "admin123"
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Wait for login button and click
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# 3. Validate the page title
expected_title = "OrangeHRM"
time.sleep(2)  # Wait for a few seconds to ensure page load
actual_title = driver.title

if actual_title == expected_title:
    print(f"Test Passed: Page title is '{expected_title}'.")
else:
    print(f"Test Failed: Page title is '{actual_title}' instead of '{expected_title}'.")

# 4. Go to Admin page
admin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
admin_button.click()

# 5. Validate that the required Admin Page Headers are displayed

# List of expected headers
expected_headers = [
    "User Management", 
    "Job", 
    "Organization", 
    "Qualifications", 
    "Nationalities", 
    "Corporate Banking", 
    "Configuration"
]

# Check if each header is visible on the page
for header in expected_headers:
    try:
        # Locate the header by text
        header_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{header}']")))
        print(f"{header}' is not displayed.")
    except:
        print(f"{header}' is  displayed.")



# 7. Quit the browser
driver.quit()
