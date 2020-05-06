#!/usr/bin/python3
from hardware_client.hardware_client import HardwareClient


URI = "ws://localhost:8090/ws_json"


if __name__ == "__main__":
    HardwareClient(URI).run()
