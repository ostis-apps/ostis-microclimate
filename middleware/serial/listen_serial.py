import os
import serial
import json

from utils import CONFIGFILE, DIRPATH


if __name__ == '__main__':
    config_data = None
    with open(CONFIGFILE) as json_file:
        config_data = json.load(json_file)

    arduino = serial.Serial(
        config_data['comport'],
        config_data['baudrate'],
        timeout=config_data['timeout']
    )

    while True:
        data = arduino.readline().decode('utf8')[:-2]
        with open(os.path.join(DIRPATH, 'out.json'), 'w') as outfile:
            if data != '__transmitting':
                data = json.loads(data)
                json.dump(data, outfile, indent=4)
