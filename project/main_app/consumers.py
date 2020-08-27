import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class Consumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self,close_code):
        pass

    async def recieve(self, data):
        data_json = json.loads(data)


    async def send_data(self,event):
        pass