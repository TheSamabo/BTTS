import websockets
import asyncio
import json
import time
from datetime import datetime
from GoogleTTS import tts
import random


class TTV_Websocket():
    def __init__(self):

        self.connection = None

        self.channel_id = None
        self.access_token = None
        self.isOpened = False

    async def connect(self):
        self.conn = await websockets.client.connect("wss://pubsub-edge.twitch.tv")
        print(self.conn)
        if self.conn.open:
            data = json.dumps({
                        "type":"LISTEN",
                        "data": {
                            "topics": ["channel-points-channel-v1." + self.channel_id],
                            "auth_token": self.access_token
                        }
                    })
            await self.sendMessage(data)
            return self.conn

    async def open_and_keep(self, conn):
        while(True):
                ping = json.dumps({
                    "type": "PING" })


                await self.sendMessage(ping)
                await asyncio.sleep(100 + random.randrange(1,50))
        
    async def sendMessage(self, message):
        await self.conn.send(message)


    async def listen(self, socket):    
            
            
            while(True):
                msg = await socket.recv()
                print(datetime.now(), end=" ")
                dict_msg = json.loads(msg)
                try:

                    if dict_msg["type"] == "RESPONSE" and dict_msg["error"]:
                        
                        raise dict_msg["error"]
                    elif dict_msg["type"] == "MESSAGE":
                        placeholder = json.loads(dict_msg["data"]["message"])
                        core_msg = placeholder["data"]["redemption"]["user_input"]
                        userFrom_msg = placeholder["data"]["redemption"]["user"]["display_name"]
                        print(dict_msg)
                        say_text = "%s says %s" % (userFrom_msg,core_msg)
                        tts(say_text)
                        
                    else:
                        print(dict_msg)

                except Exception as e:
                    print(e)
                    loop.stop()
    def Start(self):
       
        loop = asyncio.get_event_loop()
        
        self.connection = loop.run_until_complete(self.connect())
        tasks = [ 
                asyncio.ensure_future(self.open_and_keep(self.connection)),
                asyncio.ensure_future(self.listen(self.connection))
            ]
                
        loop.run_until_complete(asyncio.wait(tasks))
