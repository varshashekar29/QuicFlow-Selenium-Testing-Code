import os
from login_helper import perform_login, driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.webdriver.common.keys import Keys

source_connector_name = os.getenv("source_connector")
source_url = os.getenv("source_instance_url")
source_email_id = os.getenv("source_email")
source_api_token = os.getenv("source_api_token")
destination_connector_name = os.getenv("destination_connector")
destination_url = os.getenv("destination_instance_url")
destination_email_id = os.getenv("destination_email")
destination_api_token = os.getenv("destination_api_token")

def test_connection(driver):
    perform_login(driver)    
    
    connection_link =  WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Connections']/parent::a")) )
    connection_link.click()
    logging.info("Navigated to the connection Page")
    
    add_connection_button = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-primary")))
    add_connection_button.click()
    logging.info("Add connection button clicked")
    
    connection_name_input=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Connection Name']")))
    connection_name_input.clear()
    connection_name_input.send_keys("Selenium Connection Creation")
    logging.info("Connection name entered")
    
    region=WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-6-placeholder']")))
    region.click()
    logging.info("Region dropdown clicked")
    region_option= WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select__option')]")))
    region_option.click()
    logging.info("Region selected")
    
    
    # Source Connector Details
    
    source_connector = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-7-input']")))
    source_connector.click()
    logging.info("Source Connector dropdown clicked")
    source_connector.send_keys(source_connector_name)
    source_connector.send_keys(Keys.ENTER)
    logging.info("Source Connector selected")   
    time.sleep(8)
    source_instance_url = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'][placeholder='Enter Jira URL']"))
)
    source_instance_url.clear()
    source_instance_url.send_keys(source_url)
    logging.info("Source Instance URL entered")

    time.sleep(8)
    # source_email = WebDriverWait(driver, 15).until(
    # EC.presence_of_element_located((By.XPATH, "//input[@type='email' and @placeholder='Enter your email']")))
    # source_email.clear()
    # source_email.send_keys(source_email_id)
    # logging.info("Source Email entered")
    # time.sleep(2)
    # source_api_token = WebDriverWait(driver, 15).until(
    # EC.presence_of_element_located((By.XPATH, "//input[@type='password' and @placeholder='Enter API token']")))
    # source_api_token.clear()
    # source_api_token.send_keys(source_api_token)
    # logging.info("Source API Token entered")
    # time.sleep(2)
    # test_source_connection =  WebDriverWait(driver, 15).until(
    # EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Test Connection']")))
    # test_source_connection.click()


#Destination Connector Details

    # destination_connector = WebDriverWait(driver, 15).until(
    # EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-8-input']")))
    # destination_connector.click()
    # logging.info("Destination Connector dropdown clicked")
    # destination_connector.send_keys(destination_connector_name)
    # destination_connector.send_keys(Keys.ENTER)
    # logging.info("Destination Connector selected")
    # destination_instance_url = WebDriverWait(driver, 15).until(
    # EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @placeholder='Enter Jira URL']")))
    # destination_instance_url.send_keys("destination_url")
    # logging.info("Destination Instance URL entered")
    # destination_email = source_email = WebDriverWait(driver, 15).until(
    # EC.presence_of_element_located((By.XPATH, "//input[@type='email' and @placeholder='Enter your email']")))
    # destination_email.clear()
    # destination_email.send_keys(destination_email_id)
    # logging.info("Destination Email entered")
    # destination_api_token = WebDriverWait(driver, 15).until(
    # EC.presence_of_element_located((By.XPATH, "//input[@type='password' and @placeholder='Enter API token']")))
    # destination_api_token.clear()
    # destination_api_token.send_keys(destination_api_token)
    # logging.info("Destination API Token entered")
    # test_destination_connection =  WebDriverWait(driver, 15).until(
    # EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Test Connection']")))
    # test_destination_connection.click()

    
    
    time.sleep(8)