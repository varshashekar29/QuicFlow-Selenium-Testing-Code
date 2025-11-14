import os
from helpers.login_helper import perform_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.webdriver.common.keys import Keys

connection_name = "Selenium Connection Creation"

def navigate_to_connection_page(driver):
    """Navigate to the Connections page"""
    connection_link =  WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Connections']/parent::a")) )
    connection_link.click()
    logging.info("Navigated to the connection Page")

def enable_connection(driver, connection_name):
    """Enable the connection"""
    perform_login(driver)
    navigate_to_connection_page(driver)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//table")))
    time.sleep(1)  # Optional: allow table to fully render

    try:
        connection_row = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, f"//tr[td//*[contains(text(), '{connection_name}')]]")))
    except Exception as e:
        logging.error(f"Could not find connection row for: {connection_name}")
        raise e

    toggle_switch = connection_row.find_element(By.XPATH, ".//div[contains(@class, 'cursor-pointer') and contains(@class, 'rounded-full')]")
    toggle_switch.click()
    logging.info(f"Connection enabled for: {connection_name}")

    time.sleep(0.5)

    # Click Yes, Enable
    yes_enable_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(., 'Yes') and contains(., 'Enable')]"
        ))
    )

    yes_enable_button.click()


def configure_connection(driver, connection_name):
    """Configure Connection"""
    perform_login(driver)
    navigate_to_connection_page(driver)  

    # Wait for the table to load
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//table")))
    time.sleep(2)  # Allow table to fully render
    
    # Find the connection row - try multiple approaches
    try:
        # Approach 1: Look for connection name in any table cell
        connection_row = driver.find_element(By.XPATH, f"//td[contains(text(), '{connection_name}')]/parent::tr")
    except:
        try:
            # Approach 2: Look for connection name anywhere in the row
            connection_row = driver.find_element(By.XPATH, f"//tr[.//text()[contains(., '{connection_name}')]]")
        except:
            # Approach 3: Find by partial text match
            connection_row = driver.find_element(By.XPATH, f"//tr[contains(., '{connection_name}')]")
    
    logging.info(f"Found connection row for: {connection_name}")
    
    # Find and click the gear button in the Action column
    try:
        gear_button = connection_row.find_element(By.XPATH, ".//button[contains(@class, 'MuiIconButton-root')]")
        gear_button.click()
        logging.info("Clicked gear icon successfully")
    except:
        # Alternative: Find gear by SVG attributes
        gear_button = connection_row.find_element(By.XPATH, ".//svg[@data-icon='gear']/parent::button")
        gear_button.click()
        logging.info("Clicked gear icon (alternative method)")
    time.sleep(0.5)
    configure_menu_item = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//li[@role='menuitem' and normalize-space(text())='Configure']"
    ))
)
    configure_menu_item.click()


def disable_connection(driver, connection_name):
    perform_login(driver)
    navigate_to_connection_page(driver)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//table")))
    time.sleep(1)  # Optional: allow table to fully render

    try:
        connection_row = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, f"//tr[td//*[contains(text(), '{connection_name}')]]")))
    except Exception as e:
        logging.error(f"Could not find connection row for: {connection_name}")
        raise e

    toggle_switch = connection_row.find_element(By.XPATH, ".//div[contains(@class, 'cursor-pointer') and contains(@class, 'rounded-full')]")
    toggle_switch.click()
    logging.info(f"Connection enabled for: {connection_name}")

    # Wait for the modal/dialog to appear
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'group') and contains(@class, 'relative')]"))
    )

    # Now search for and click the "Yes, Enable" button
    yes_disable_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(., 'Yes') and contains(., 'Disable')]"
        ))
    )

    yes_disable_button.click()

    
    









