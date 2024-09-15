from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# the webdriver
driver = webdriver.Chrome()

#the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# usernhame
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

#password field
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# login button 
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

 
time.sleep(5)  

# check the menu is available 
expected_menu_items = [
        "Admin",
        "PIM",
        "Leave",
        "Time",
        "Recruitment",
        "My Info",
        "Performance",
        "Dashboard",
        "Directory",
        "Maintenance",
        "Buzz"
    ]

    # Check each menu item
for item in expected_menu_items:
    try:
           
            menu_element = driver.find_element(By.XPATH, f"//span[text()='{item}']")
            if menu_element.is_displayed():
                print(f"{item} menu option is displayed.")
            else:
                print(f"{item} menu option is not displayed.")
    except:
            print(f"{item} menu option is not found.")

driver.quit()
