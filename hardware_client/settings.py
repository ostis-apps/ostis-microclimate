import os


DIRPATH =  os.path.dirname(os.path.realpath(__file__))
CONFIGFILE = os.path.join(DIRPATH, 'configs.json')
CONFIG_FIELDNAMES = ['port', 'baudrate', 'timeout']
