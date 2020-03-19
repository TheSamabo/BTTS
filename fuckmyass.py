import websockets
import asyncio
import json
import time
from GoogleTTS import tts

isGettingMessage = True
access_token = "3chzarzuypzcfnabl1o4hnkqwkm9bj"
channel_id = "66504977"

url = "wss://pubsub-edge.twitch.tv"
loop = asyncio.get_event_loop()

async def open_and_keep():

    async with websockets.connect(url) as socket:
        ping = json.dumps({
            "type": "PING" })

        await socket.send(ping)
        res = await socket.recv()
        print(res)
    

    


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
        if dec_resp["error"]:
            loop.stop()
        else:
            print("Successfuly connected")
            
        while(loop.is_running):
            
            msg = await socket.recv()
            #startingPoint = text_ts.find("status")
            dec_msg = json.loads(json.loads(msg[81:len(msg) - 4]))
            tts_msg = dec_msg["data"]["redemption"]["user_input"]
            tts_user = dec_msg["data"]["redemption"]["user"]["display_name"]
            tts_text = tts_user + " says, " + tts_msg
            print( tts_user + "'s Input: " + tts_msg)

            tts(tts_text)
            now_min = time.gmtime()[4]
            now_sec= time.gmtime()[5]

            # print(now_sec)
            if str(now_min)[0] == "0":
                lig = str(now_min)[1]
                
            else:
                lig = str(now_min)[0]


            if lig == "2" or lig == "4" or lig == "6" or lig == "8":
                if str(now_sec) == "1" or str(now_sec) == "2":
                    await asyncio.wait(open_and_keep,None)


            # os.system('espeak ' tts)
            #await os.system("espeak " + text_ts["data"]["message"]["data"]["redemption"]["user_input"])       
async def ping():
    await open_and_keep()    
    
loop.run_until_complete(open_and_keep())

loop.run_until_complete(listen())

# loop.run_until_complete(test())

 