import asyncio
import websockets

async def hello():
    uri = "ws://<YOUR_SERVER_IP>:8765"  # แทนที่ <YOUR_SERVER_IP> เป็น IP address ของเซิร์ฟเวอร์
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        response = await websocket.recv()
        print(f"< {response}")

asyncio.run(hello())
