import os
import json
from helpers.connection_helper import configure_connection,load_project_mapping, load_record_type_mapping, project_mapping_gear_icon, record_type_mapping, record_type_mapping_gear_icon, adding_trigger_sync_source_jql, adding_trigger_sync_destination_jql

connection_name = os.getenv("connection_name")

with open("mapping_config.json", "r") as f:
    config = json.load(f)
source_project_name = config['project_mapping']['source_project_name']
source_record_type = config['record_type_mapping']['source_record_type']
destination_record_type = config['record_type_mapping']['destination_record_type']
trigger_sync_source_jql = config['trigger_sync_source_jql']
trigger_sync_destination_jql = config['trigger_sync_destination_jql']


def test_record_type_mapping(logged_in_driver):    
    configure_connection(logged_in_driver, connection_name)
    project_mapping_gear_icon(logged_in_driver, source_project_name)
    load_record_type_mapping(logged_in_driver) 
    record_type_mapping(logged_in_driver, source_record_type, destination_record_type)

def test_trigger_sync_jql(logged_in_driver):
    configure_connection(logged_in_driver, connection_name)
    project_mapping_gear_icon(logged_in_driver, source_project_name)
    load_record_type_mapping(logged_in_driver) 
    adding_trigger_sync_source_jql(logged_in_driver, trigger_sync_source_jql)
    adding_trigger_sync_destination_jql(logged_in_driver, trigger_sync_destination_jql)

def test_record_type_mapping_gear_icon(logged_in_driver):
    configure_connection(logged_in_driver, connection_name)
    project_mapping_gear_icon(logged_in_driver, source_project_name)
    load_record_type_mapping(logged_in_driver) 
    record_type_mapping_gear_icon(logged_in_driver, source_record_type)
   



    


