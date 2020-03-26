#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json

class tw_pubsub():

    async def open(self, data):
       self.url = "wss://pubsub-edge.twitch.tv"
       async with websockets.connect(self.uri) as pubsub:

       
       
       
       
       
       
       
       
       
       
       
       
       
        # self.uri = "wss://pubsub-edge.twitch.tv"
        # async with websockets.connect(self.uri) as pubsub:
        #     self.data = json.dumps({
        #             "type":"LISTEN",
        #             "data": {
        #                 "topics": ["channel-points-channel-v1.66504977"],
        #                 "auth_token": "114ldkrwjul2y8ksja0evzevzlxhru"
        #             }
        #         })
        #     await pubsub.send(self.data)
        #     self.resp = await pubsub.recv()
                    
        #     print(self.resp)


    async def test():
        async with websockets.connect("wss://pubsub-edge.twitch.tv"):
            pinging = json.dumps({"type": "PING"})
            await socket.send(pinging)
            test_resp = await socket.recv()
            print(test_resp)

ligma = tw_pubsub()

# asyncio.get_event_loop().run_until_complete(ligma.test())
# asyncio.get_event_loop().run_until_complete(ligma.open())
asyncio.get_event_loop().run_forever(ligma.test())
'''
asyncio.get_event_loop().run_forever()
'''

    




