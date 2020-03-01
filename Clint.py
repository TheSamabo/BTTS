#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json


async def open():
    uri = "wss://pubsub-edge.twitch.tv"
    async with websockets.connect(uri) as socket:
        data = json.dumps({
            "type":"LISTEN",
            "data": {
                "topics": ["channel-points-channel-v1.66504977"],
                "auth_token": "46emmdbbto5srlmcvfy2tzxwwj6dij"
            }
        })
        await socket.send(data)
        resp = await socket.recv()
        print(resp)


async def test():
    async with websockets.connect("wss://pubsub-edge.twitch.tv") as socket:
        pinging = json.dumps({"type": "PING"})
        await socket.send(pinging)
        resp = await socket.recv()
        print(resp)


asyncio.get_event_loop().run_until_complete(open())
'''
asyncio.get_event_loop().run_forever()
'''

    




