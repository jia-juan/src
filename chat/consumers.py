# -*- coding: utf-8 -*-
import json

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


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
