import asyncio
import websockets

from micro_controller_connection import MicroControllerConnection, MicroControllerConnectionError
from serializers import ComportSerializer


class HardwareClient:
    def __init__(self, uri):
    self.mk_connection = MicroControllerConnection()
    self.uri = uri

    try:
        self.mk_connection.connect()
    except MicroControllerConnectionError:
        # The last attempt to reconnect. There are sometimes issues
        # with connection from the first time
        self.mk_connection.connect()

    async def send_microclimate_parameters(self, data):
        async with websockets.connect(self.uri) as websocket:
            await websocket.send(data)

            response = await websocket.recv()
            print(response)

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.send_microclimate_parameters())    
