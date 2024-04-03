# mapapp/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LostKidConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']

        if message_type == 'lost_kid':
            await self.send(text_data=json.dumps({
                'type': 'popup',
                'content': 'A child is missing!',
            }))
