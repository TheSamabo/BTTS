import websockets
import asyncio
import json
import time
from datetime import datetime
from GoogleTTS import tts
from auth_url import twitch_api
import random

isGettingMessage = True
access_token = "n9eszb4g3ms09xd5l2s3ihhs8ch865"
channel_id = "66504977"

url = "wss://pubsub-edge.twitch.tv"

class TTV_Websocket():
    def __init__(self):
        pass
    async def connect(self):
        self.conn = await websockets.client.connect(url)
        print(self.conn)
        if self.conn.open:
            data = json.dumps({
                        "type":"LISTEN",
                        "data": {
                            "topics": ["channel-points-channel-v1." + channel_id],
                            "auth_token": access_token
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
                if dict_msg["type"] == "MESSAGE":
                    placeholder = json.loads(dict_msg["data"]["message"])
                    core_msg = placeholder["data"]["redemption"]["user_input"]
                    tts(core_msg)
                    
                    print(core_msg)
                elif dict_msg["error"]:
                    print("Error: "  + dict_msg["error"])
                    loop.stop()
                    break
                else:
                    print(msg)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    q = TTV_Websocket()
    connection = loop.run_until_complete(q.connect())
    tasks = [ 
            asyncio.ensure_future(q.open_and_keep(connection)),
            asyncio.ensure_future(q.listen(connection))
        ]
            
    loop.run_until_complete(asyncio.wait(tasks))
