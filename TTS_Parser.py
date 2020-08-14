import websockets
import asyncio
import json
import time
from datetime import datetime
from GoogleTTS import tts
import random
import logging
from Components.auth.Auth import checkData

loop = asyncio.get_event_loop()
class TTV_Websocket():
    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.connection = None

        self.channel_id = checkData(True)["ChannelId"]
        self.access_token = checkData(True)["AccessToken"] 
        self.ttsName = "Text to Speech"

    async def connect(self):
        self.conn = await websockets.client.connect("wss://pubsub-edge.twitch.tv")
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
        while(loop.is_running()):
                ping = json.dumps({
                    "type": "PING" })


                await self.sendMessage(ping)
                await asyncio.sleep(50 + random.randrange(1,50))
        
        
    async def sendMessage(self, message):
        await self.conn.send(message)


    async def listen(self, socket):    
            
            
        try:
            while(loop.is_running()):
                msg = await socket.recv()
                print(datetime.now(), end=" ")
                dict_msg = json.loads(msg)

                if dict_msg["type"] == "RESPONSE" and dict_msg["error"]:
                    
                    raise dict_msg["error"]
                elif dict_msg["type"] == "MESSAGE":
                    placeholder = json.loads(dict_msg["data"]["message"])

                    # Check the name of the reward
                    if placeholder["data"]["redemption"]["reward"]["title"] == self.ttsName:

                        core_msg = placeholder["data"]["redemption"]["user_input"]
                        userFrom_msg = placeholder["data"]["redemption"]["user"]["display_name"]
                        print(dict_msg)
                        say_text = "%s says %s" % (userFrom_msg,core_msg)
                        tts(say_text)
                    
                else:
                        print(dict_msg)


        except Exception as e:
            self.logger.exception(e)
            print(e)
            loop.stop()
        
    def Stop(self):
        self.logger.warn("Closing TTS")
        loop.close()

    def Start(self):
       
        
        self.connection = loop.run_until_complete(self.connect())
        tasks = [ 
                asyncio.ensure_future(self.open_and_keep(self.connection)),
                asyncio.ensure_future(self.listen(self.connection))
            ]
                
        loop.run_until_complete(asyncio.wait(tasks))
