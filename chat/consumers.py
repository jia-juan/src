# -*- coding: utf-8 -*-
import json

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
            # self.user_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


class EchoConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            'type': "websocket.accept"
        })

    async def websocket_receive(self, event):
        # ORM 異步查詢範例
        # ISSUE: 終於成功版，使用asgiref.sync sync_to_async()
        # ref: https://stackoverflow.com/questions/63892884/django-channels-async-websocket-throwing-error-while-trying-to-use-database-quer
        resp = json.loads(event['text'])
        # es = await sync_to_async(ElasticSetting.objects.get)(name=resp['name'])

        await self.send({
            "type": "websocket.send",
            "text": resp['name']
        })
