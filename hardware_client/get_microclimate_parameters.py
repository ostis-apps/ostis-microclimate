#!/usr/bin/python3
import os
import json
import asyncio
import websockets

import settings
from hardware_client import IDTFReceiver

IDTF = [
    'microclimate_record',
    'humidity',
    'temperature',
    'rrel_mesurement_time',
    'rrel_mesurement_place',
    'office',
    'nrel_value'
]


class MicroclimanteParametersRepresenter:
    def __init__(self):
        self.idtfs = IDTFReceiver(IDTF).idtf_ids

    def represent(self):
        asyncio.get_event_loop().run_until_complete(self._get_link_data())

    async def _get_link_data(self):
        async with websockets.connect(settings.URI) as websocket:
            with open(os.path.join(settings.DIRPATH, 'log.json')) as json_file: 
                logs = json.load(json_file)

            for log in logs:
                data = {'id': 15, 'type': 'content', 'payload': [
                    {
                        'command': 'get', 'addr': log['date_link_addr']
                    },
                    {
                        'command': 'get', 'addr': log['humi_link_addr']
                    },
                    {
                        'command': 'get', 'addr': log['temp_link_addr']
                    }
                ]}
    
                await websocket.send(json.dumps(data))

                response = await websocket.recv()
                print(response)


if __name__ == '__main__':
    MicroclimanteParametersRepresenter().represent()
