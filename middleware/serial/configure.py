import sys
import glob
import serial
import json
import time

import tqdm

from utils import get_configs, CONFIGFILE


if __name__ == '__main__':
    configs = get_configs()
    baudrate = configs['baudrate']
    timeout = configs['timeout']

    if sys.platform.startswith('win'):
        ports = ['COM{}'.format(i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    else:
        raise EnvironmentError('Unsupported platform')
    
    arduino = None
    workport = None
    for port in tqdm.tqdm(ports):
        try:
            arduino = serial.Serial(port, baudrate, timeout=timeout)
        except (OSError, serial.SerialException):
            pass
        else:
            if arduino.readline() == b'__transmitting\r\n':
                arduino.flushInput()
                arduino.write(b'__recieved')

                config_data = {
                    'baudrate': baudrate,
                    'timeout': timeout,
                    'comport': port,
                }

                with open(CONFIGFILE, 'w') as outfile:
                    json.dump(config_data, outfile, indent=4)
                
                workport = port
                arduino.close()

    if workport:
        print('Working with {}, {} baudrate'.format(workport, baudrate))
    else:
        print('Failed')
