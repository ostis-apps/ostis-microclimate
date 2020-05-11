import os


DIRPATH =  os.path.dirname(os.path.realpath(__file__))
CONFIGFILE = os.path.join(DIRPATH, 'configs.json')
CONFIG_FIELDNAMES = ['port', 'baudrate', 'timeout']
IDTF = [
    'microclimate_record',
    'humidity',
    'temperature',
    'rrel_mesurement_time',
    'rrel_mesurement_place',
    'nrel_percental_mesurement',
    'nrel_celsius_mesurement',
    'office',
    'value',
    'number',
    'nrel_value'
]