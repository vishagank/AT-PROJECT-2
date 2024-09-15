from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# webdriver to action
driver = webdriver.Chrome()

# Launch the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# the "Forgot Password" link to be clickable
forgot_password_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Forgot your password? ']")))

forgot_password_link.click()

# username textbox to be visible
username_textbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

username_textbox.send_keys("vishal")

#  Reset Password button
reset_password_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
reset_password_button.click()

time.sleep(2)

#to check the test case result
try:
    login_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h5[text()='Reset Password']"))
    )
    print("Reset Password link was not sent successfully.")
except:
    print("Reset Password link sent successfully.")


time.sleep(2)

driver.quit()
