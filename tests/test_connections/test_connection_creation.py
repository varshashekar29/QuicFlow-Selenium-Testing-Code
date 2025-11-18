import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.webdriver.common.keys import Keys
from helpers.connection_helper import navigate_to_connection_page

source_connector_name = os.getenv("source_connector")
source_url = os.getenv("source_instance_url")
source_email_id = os.getenv("source_email")
source_token = os.getenv("source_api_token")
destination_connector_name = os.getenv("destination_connector")
destination_url = os.getenv("destination_instance_url")
destination_email_id = os.getenv("destination_email")
destination_token = os.getenv("destination_api_token")
connection_name_given = os.getenv("connection_name")

def test_connection(logged_in_driver):    
    navigate_to_connection_page(logged_in_driver)    
    
    add_connection_button = WebDriverWait(logged_in_driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-primary")))
    add_connection_button.click()
    logging.info("Add connection button clicked")
    
    connection_name_input=WebDriverWait(logged_in_driver,15).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Connection Name']")))
    connection_name_input.clear()
    connection_name_input.send_keys(connection_name_given)
    logging.info("Connection name entered")
    
    region=WebDriverWait(logged_in_driver,15).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-6-placeholder']")))
    region.click()
    logging.info("Region dropdown clicked")
    region_option= WebDriverWait(logged_in_driver,15).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select__option')]")))
    region_option.click()
    logging.info("Region selected")     
    
#     # Source Connector Details
    source_connector_dropdown = WebDriverWait(logged_in_driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,  "//div[@id='react-select-7-placeholder']/parent::div")))
    source_connector_dropdown.click()
    logging.info("Source Connector dropdown clicked")    
    source_connector_input = WebDriverWait(logged_in_driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='react-select-7-input']")))
    time.sleep(3)
    source_connector_input.send_keys(source_connector_name)
    source_connector_input.send_keys(Keys.ENTER)
    logging.info("Source Connector selected")   
    time.sleep(3)
    source_instance_url = WebDriverWait(logged_in_driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@name='url' and @type='text' and @placeholder='Enter Jira URL'])[1]")))
    source_instance_url.clear()
    time.sleep(3)
    source_instance_url.send_keys(source_url)
    logging.info("Source Instance URL entered")

    source_email = WebDriverWait(logged_in_driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='email' and @placeholder='Enter your email'])[1]")))
    source_email.clear()
    source_email.send_keys(source_email_id)
    logging.info("Source Email entered")
    source_api_token = WebDriverWait(logged_in_driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@name='token' and @type='password' and @placeholder='Enter API token'])[1]")))
    source_api_token.clear()
    source_api_token.send_keys(source_token)
    logging.info("Source API Token entered")
    test_source_connection =  WebDriverWait(logged_in_driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Test Connection'])[1]")))
    test_source_connection.click()
    source_success_message_alert = WebDriverWait(logged_in_driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='Source Connection Successful']")))
    print(source_success_message_alert)
    assert "Source Connection Successful" in source_success_message_alert.text
    time.sleep(0.5)

# Destination Connector Details
    destination_connector = WebDriverWait(logged_in_driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-8-input']")))
    destination_connector.click()
    logging.info("Destination Connector dropdown clicked")
    destination_connector.send_keys(destination_connector_name)
    destination_connector.send_keys(Keys.ENTER)
    logging.info("Destination Connector selected")
    destination_instance_url = WebDriverWait(logged_in_driver, 15).until(EC.presence_of_element_located((By.XPATH, "(//input[@name='url' and @type='text' and @placeholder='Enter Jira URL'])[2]")))
    destination_instance_url.clear()
    destination_instance_url.send_keys(destination_url)
    logging.info("Destination Instance URL entered")
    destination_email = WebDriverWait(logged_in_driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='email' and @placeholder='Enter your email'])[2]")))
    destination_email.clear()
    destination_email.send_keys(destination_email_id)
    logging.info("Destination Email entered")
    destination_api_token = WebDriverWait(logged_in_driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='password' and @placeholder='Enter API token'])[2]")))
    destination_api_token.clear()
    destination_api_token.send_keys(destination_token)
    logging.info("Destination API Token entered")
    test_destination_connection =  WebDriverWait(logged_in_driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Test Connection'])[2]")))
    test_destination_connection.click()
    destination_success_message_alert = WebDriverWait(logged_in_driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='Destination Connection Successful']")))
    assert "Destination Connection Successful" in destination_success_message_alert.text
    logging.info("Destination connection successful")
    time.sleep(4)

# Save connection
    save_connection_button = WebDriverWait(logged_in_driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save Connection']")))
    save_connection_button.click()    
    logging.info("Connection Saved Successfully")
    save_connection_success_alert = WebDriverWait(logged_in_driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='notistack-snackbar' and contains(text(),'Connection Saved Successfully')]")))
    assert "Connection Saved Successfully" in save_connection_success_alert.text
    logging.info("Connection saved successfully")
    time.sleep(0.5)