import os
from dotenv import load_dotenv
from helpers.login_helper import perform_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.webdriver.common.keys import Keys
from helpers.connection_helper import enable_connection, configure_connection, disable_connection

load_dotenv()

def test_enable_connection(driver):
    connection_name = os.getenv("connection_name")
    enable_connection(driver, connection_name)
    time.sleep(8)

def test_connection_configure(driver):
    connection_name = os.getenv("connection_name")
    configure_connection(driver, connection_name)
    time.sleep(8)

def test_disable_connection(driver):
    connection_name = os.getenv("connection_name")
    disable_connection(driver, connection_name)
    time.sleep(8)



