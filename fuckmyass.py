import websockets
import asyncio
import json
import time
from GoogleTTS import tts

isGettingMessage = True
access_token = "j9gmn6e9l29c9swrfc9sw1qbewcs84"
channel_id = "66504977"

url = "wss://pubsub-edge.twitch.tv"
loop = asyncio.get_event_loop()

async def open_and_keep():
    while(True):
        async with websockets.connect(url) as socket:
            ping = json.dumps({
                "type": "PING" })

            await socket.send(ping)
            res = await socket.recv()
            print(res)
            await asyncio.sleep(120)
    

    


async def listen():    
    async with websockets.connect(url) as socket:
        data = json.dumps({
                    "type":"LISTEN",
                    "data": {
                        "topics": ["channel-points-channel-v1." + channel_id],
                        "auth_token": access_token
                    }
                })
        await socket.send(data)
        resp = await socket.recv()
        dec_resp = json.loads(resp)
        print(dec_resp)
       
        while(loop.is_running):
            
            msg = await socket.recv()
            #startingPoint = text_ts.find("status")
            dec_msg = json.loads(json.loads(msg[81:len(msg) - 4]))
            tts_msg = dec_msg["data"]["redemption"]["user_input"]
            tts_user = dec_msg["data"]["redemption"]["user"]["display_name"]
            tts_text = tts_user + " says, " + tts_msg
            print( tts_user + "'s input: " + tts_msg)

            tts(tts_text)
            

            # os.system('espeak ' tts)
            #await os.system("espeak " + text_ts["data"]["message"]["data"]["redemption"]["user_input"])       
    
loop.create_task(open_and_keep())

loop.run_until_complete(listen())

# loop.run_until_complete(test())

 