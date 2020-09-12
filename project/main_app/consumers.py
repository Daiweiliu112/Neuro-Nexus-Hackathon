import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class Consumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #self.room_name = 'test'
        
        self.room_group_name = 'session_%s' % self.room_name
        print("self scope: " + self.scope['url_route']['kwargs']['room_name'])
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        

    async def recieve(self, data):
        data_json = json.loads(data)
        message = data_json['message']
        print("message:" + message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message

            }
        )


    async def chat_message(self,event):
        message = event['message']
        print("testing sending")
        await self.send(text_data= json.dumps({
            'message':message
        }))