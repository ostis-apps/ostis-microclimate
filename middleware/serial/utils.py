import os
import json


DIRPATH =  os.path.dirname(os.path.realpath(__file__))
CONFIGFILE = os.path.join(DIRPATH, 'configs.json')
CONFIG_FIELDNAMES = ['port', 'baudrate', 'timeout']

def get_configs():
    configs = dict()
    with open(CONFIGFILE) as json_file:
        config_data = json.load(json_file)
        for field_name in CONFIG_FIELDNAMES:
            try:
                configs.update({field_name: config_data[field_name]})
            except KeyError:
                configs.update({field_name: None})
    
    return configs
