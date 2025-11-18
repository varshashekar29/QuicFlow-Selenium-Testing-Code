import os
import json
from helpers.connection_helper import configure_connection,load_project_mapping, load_record_type_mapping, project_mapping_gear_icon


with open("mapping_config.json", "r") as f:
    config = json.load(f)
source_project_name = config['project_mapping']['source_project_name']


def test_record_type_mapping(logged_in_driver):
    connection_name = os.getenv("connection_name")
    # configure_connection(logged_in_driver, connection_name)
    # load_project_mapping(logged_in_driver)
    # project_mapping_gear_icon(logged_in_driver, source_project_name)
    # load_record_type_mapping(logged_in_driver)
    # print("--------------------------------------------")


