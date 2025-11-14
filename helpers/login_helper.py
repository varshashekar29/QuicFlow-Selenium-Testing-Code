import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")   

# Load environment variables
load_dotenv(override=True)
login_url = os.getenv("login_url")
username = os.getenv("username")
password = os.getenv("password")

def perform_login(driver):
        driver.get(login_url)
        username_field=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.clear()
        username_field.send_keys(username)
        logging.info("Username is added")

        password_field=password_field = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password'][placeholder='Password']"))
)
        password_field.clear()
        password_field.send_keys(password)
        logging.info("Password is added")

        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
        )
        login_button.click()
        logging.info("Logged in successfully")
        
        org_lunching_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Launch'])[2]")))
        assert org_lunching_button is not None, "Second 'Launch' button not found"
        org_lunching_button.click()
        logging.info("Second 'Launch' button clicked")  