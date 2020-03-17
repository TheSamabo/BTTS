import websockets
import asyncio
import json

url = "wss://pubsub-edge.twitch.tv"
loop = asyncio.get_event_loop()
async def open():
    async with websockets.connect(url) as socket:
        ping = json.dumps({
            "type": "PING"
        })
        await socket.send(ping)
        res = await socket.recv()
        print(res)
        
async def ligma():    
    async with websockets.connect(url) as socket:
        data = json.dumps({
                    "type":"LISTEN",
                    "data": {
                        "topics": ["channel-points-channel-v1.66504977"],
                        "auth_token": "p7eemhelxosvr1yqmk4bi361qn3vzj"
                    }
                })
        await socket.send(data)
        resp = await socket.recv()
        print(resp)

        while(True):
            msg = await socket.recv()
            text_ts =  await json.loads(msg)
            print(text_ts["user_input"])
       

loop.run_until_complete(open())
loop.run_until_complete(ligma())

