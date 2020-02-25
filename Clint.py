#!/usr/bin/env python

# WS client example

import asyncio
from websockets import client
import json

async with ws.websocket

await def open(ws):
    uri = "wss://pubsub-edge.twitch.tv"
    async ws.connect(uri)

await def recv(ws):
    msg = await ws.recv()

def test(ws):
    ping = json.dumps({"type": "PING"})
    ws.send(ping)


async get_event_loop().run_until_complete(test())


    








'''
async def hello():
    uri = "wss://pubsub-edge.twitch.tv"
    async with websockets.connect(uri) as websocket:
        data = json.dumps({
            "type":"LISTEN",
            "data": {
                "topics": ["channel-points-channel-v1.66504977"],
                "auth_token": "kintzrnfggusiqqcc314ffjn9rralh"
            }
        })
        await websocket.send(data)
     

        greeting = await websocket.recv()
        print(greeting)

asyncio.get_event_loop().run_until_complete(hello())

asyncio.get_event_loop().run_forever(hello())
'''