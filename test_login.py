import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from login_helper import perform_login

#Configuring logging to show INFO level messages
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")




def test_valid_login(driver):
    perform_login(driver)               
        
    logging.info("Login Test completed successfully") 
    time.sleep(5)
#No try catch blocks are used here to allow pytest to capture exceptions and report them appropriately.



        
    