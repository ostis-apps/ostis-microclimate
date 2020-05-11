#!/usr/bin/python3
from hardware_client import HardwareClient


URI = "ws://localhost:8090/ws_json"


if __name__ == "__main__":
    try:
        HardwareClient(URI).run()
    except ConnectionRefusedError:
        print('Please, run OSTIS')
