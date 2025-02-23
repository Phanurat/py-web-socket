import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(input(str("Input your box: ")))
        response = await websocket.recv()
        print(f"< {response}")

asyncio.run(hello())
