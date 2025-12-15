import os
from helpers.login_helper import perform_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import logging
import time
from selenium.webdriver.common.keys import Keys
from helpers.connection_helper import load_project_mapping, configure_connection,load_record_type_mapping, project_mapping_gear_icon, delete_project_mapping

with open("mapping_config.json", "r") as f:
    config = json.load(f)
source_project_name = config['project_mapping']['source_project_name']
connection_name = os.getenv("connection_name")

def test_project_mapping(logged_in_driver):    
    configure_connection(logged_in_driver, connection_name)
    load_project_mapping(logged_in_driver)

def test_add_record_type_mapping(logged_in_driver):
    configure_connection(logged_in_driver, connection_name)
    project_mapping_gear_icon(logged_in_driver,source_project_name)
    load_record_type_mapping(logged_in_driver)

def test_delete_project_mapping(logged_in_driver):
    configure_connection(logged_in_driver, connection_name)
    project_mapping_gear_icon(logged_in_driver,source_project_name)
    delete_project_mapping(logged_in_driver)

def test_bulk_sync(logged_in_driver):
    logging.info("Yet to write code")



    

    


