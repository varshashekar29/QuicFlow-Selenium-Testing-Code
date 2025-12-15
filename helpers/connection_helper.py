from helpers.login_helper import perform_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.webdriver.common.keys import Keys
import json

connection_name = "Selenium Connection Creation"

def navigate_to_connection_page(driver):
    """Navigate to the Connections page"""
    connection_link =  WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Connections']/parent::a")) )
    connection_link.click()
    logging.info("Navigated to the connection Page")

def enable_connection(driver, connection_name):
    """Enable the connection"""
          
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

    yes_enable_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'Yes') and contains(., 'Enable')]")))
    yes_enable_button.click()


def configure_connection(driver, connection_name):
    """Configure Connection"""
    navigate_to_connection_page(driver)  

    # Wait for the table to load
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//table")))
    time.sleep(2)  # Allow table to fully render
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
    
    try:
        gear_button = connection_row.find_element(By.XPATH, ".//button[contains(@class, 'MuiIconButton-root')]")
        gear_button.click()
        logging.info("Clicked gear icon successfully")
    except:
        gear_button = connection_row.find_element(By.XPATH, ".//svg[@data-icon='gear']/parent::button")
        gear_button.click()
        logging.info("Clicked gear icon (alternative method)")
    time.sleep(0.5)
    configure_menu_item = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@role='menuitem' and normalize-space(text())='Configure']")))
    configure_menu_item.click()


def disable_connection(driver, connection_name):     
    navigate_to_connection_page(driver)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//table")))
    time.sleep(1)  #  allow table to fully render

    try:
        connection_row = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, f"//tr[td//*[contains(text(), '{connection_name}')]]")))
    except Exception as e:
        logging.error(f"Could not find connection row for: {connection_name}")
        raise e

    toggle_switch = connection_row.find_element(By.XPATH, ".//div[contains(@class, 'cursor-pointer') and contains(@class, 'rounded-full')]")
    toggle_switch.click()

    logging.info(f"Connection enabled for: {connection_name}")
    yes_disable_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'Yes') and contains(., 'Disable')]")))
    yes_disable_button.click()


def load_project_mapping(driver, config_path = "mapping_config.json"):
    """
    Mapping Projects
    """
    with open(config_path, "r") as f:
        config = json.load(f)

        source_project_name = config['project_mapping']['source_project_name']
        destination_project_name = config['project_mapping']['destination_project_name']

        #Assigning Source Project 
        assign_source_project_name = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-6-input' and @class='select__input']")))
        assign_source_project_name.clear()
        assign_source_project_name.send_keys(source_project_name)
        time.sleep(5)
        assign_source_project_name.send_keys(Keys.ENTER)
        time.sleep(3)
        logging.info("Source project is assigned")
        
        #Assigning Destination Project
        assign_destination_project_name = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-7-input' and @class='select__input']")))
        assign_destination_project_name.clear()
        assign_destination_project_name.send_keys(destination_project_name)
        time.sleep(3)
        assign_destination_project_name.send_keys(Keys.ENTER)
        time.sleep(1)
        logging.info("Destination project is assigned")
        #Adding Project Mapping
        add_project_mapping_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Add' and contains(@class, 'bg-primary')]")))
        add_project_mapping_button.click()
        logging.info(f"{assign_source_project_name} and {assign_destination_project_name} Projects Mapped!!!")
        time.sleep(1)
        try:
            project_mapping_success_alert = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='notistack-snackbar' and contains(text(), 'Project Mapped Successfully')]")))
            assert "Project Mapped Successfully" in project_mapping_success_alert.text
        except Exception as e:
            assert False, f"Alert not found: {e}"
            logging.info(driver.page_source)
    time.sleep(2)

def project_mapping_gear_icon(driver, assign_source_project_name):
    """Access the project mapping gear icon"""
    try:
        connection_row = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, f"//tr[.//div[contains(text(), '{assign_source_project_name}')]]")))
        logging.info("Connection row exists")
        try:
            gear_button = connection_row.find_element(By.XPATH, ".//button[contains(@class, 'MuiIconButton-root') and .//svg[@data-icon='gear']]")
            gear_button.click()
            logging.info("Clicked gear icon (svg inside button) successfully")
        except Exception as e1:
            try:
                gear_button = connection_row.find_element(By.XPATH, ".//svg[@data-icon='gear']/parent::button")
                gear_button.click()
                logging.info("Clicked gear icon (svg parent button) successfully")
            except Exception as e2:
                try:
                    gear_button = connection_row.find_element(By.XPATH, ".//button[contains(@class, 'MuiIconButton-root')]")
                    gear_button.click()
                    logging.info("Clicked gear icon (MuiIconButton-root only) successfully")
                except Exception as e3:
                    logging.error(f"Could not find gear icon button in row: {e1}, {e2}, {e3}")
                    logging.info(driver.page_source)
    except Exception as e:
        logging.error(f"Could not find connection row for BENZ1: {e}")
        logging.info(driver.page_source)
    time.sleep(8)

def delete_project_mapping(driver):
    """Delete Project Mapping"""
    delete_project_mapping = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//li[@role='menuitem' and normalize-space(text())='Delete Project Mapping']")))
    delete_project_mapping.click()
    delete_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Delete' and contains(@class, 'bg-error')]")))
    delete_button.click()
    logging.info("Project Mapping Deleted Successfully!!!")
    time.sleep(5)
        
def load_record_type_mapping(driver):
    """Getting into Record Types from the project mapping gear icon -> Add Record Type mapping"""
    add_record_type_mapping = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@role='menuitem' and (normalize-space(text())='Add Record Type Mapping' or normalize-space(text())='Edit Record Type Mapping')]")))
    add_record_type_mapping.click()
    logging.info("Add record type is clicked")    
    time.sleep(5)   

def record_type_mapping(driver, source_record_type,destination_record_type):
    """Mapping Record Types"""
    source_record_type_input = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-8-input' and contains(@class, 'select__input')]")))
    source_record_type_input.send_keys(source_record_type)
    time.sleep(2)
    source_record_type_input.send_keys(Keys.ENTER)
    logging.info("Source record type is selected")
    time.sleep(3)
    destination_record_type_input = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-9-input' and contains(@class, 'select__input')]")))
    destination_record_type_input.send_keys(destination_record_type)
    time.sleep(2)
    destination_record_type_input.send_keys(Keys.ENTER)
    logging.info("Destination record type is selected")
    time.sleep(3)
    add_mapping_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Add Mapping' and contains(@class, 'bg-primary')]")))
    time.sleep(4)
    add_mapping_button.click()
    logging.info("Record Type is mapped")
    try:
        record_type_mapping_success_alert = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='notistack-snackbar' and contains(text(), 'Record Type Mapped Successfully')]")))
        assert "Record Type Mapped Successfully" in record_type_mapping_success_alert.text
        logging.info("validated")
    except Exception as e:
            assert False, f"Alert not found: {e}"
            logging.info(driver.page_source)
    
    time.sleep(2)

def adding_trigger_sync_source_jql(driver, trigger_sync_source_jql):
    trigger_sync_jql_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'text-gray-400') and normalize-space(text())='JQL']")))
    trigger_sync_jql_input.click()
    logging.info("Source JQL input box is clicked")
    jql_input_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='JQL']")))
    jql_input_box.clear()
    jql_input_box.send_keys(trigger_sync_source_jql)   
    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Save' and contains(@class, 'px-3') and contains(@class, 'py-1')]")))
    save_button.click()
    logging.info("Source JQL is saved")
    time.sleep(3)

def adding_trigger_sync_destination_jql(driver,trigger_sync_destination_jql):
    trigger_sync_jql_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'text-gray-700') and .//span[normalize-space(text())='JQL']]")))
    trigger_sync_jql_input.click()
    logging.info("Destination JQL input box is clicked")
    jql_input_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//textarea[@placeholder='JQL']")))
    jql_input_box.clear()
    jql_input_box.send_keys(trigger_sync_destination_jql)   
    save_button =  WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Save' and contains(@class, 'px-3') and contains(@class, 'py-1')]")))
    save_button.click()
    logging.info("Destination JQL is saved")
    time.sleep(3)

def record_type_mapping_gear_icon(driver, source_record_type):
    """Access the record type mapping gear icon"""

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//table")))
    time.sleep(3)
    logging.info("Table loaded")
    try:
         record_row = driver.find_element(By.XPATH,f"//td[contains(text(), '{source_record_type}')]/parent::tr")
    except:
            # Approach 3: Partial match
            record_row = driver.find_element(By.XPATH,f"//tr[contains(., '{source_record_type}')]")
    logging.info(f"Found record type row for: {source_record_type}")

    gear_button = record_row.find_element(By.XPATH, ".//button[contains(@class,'MuiIconButton-root')]")
    gear_button.click()
    time.sleep(8)

    
        
               













