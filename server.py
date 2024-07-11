import asyncio
import websockets

async def echo(websocket, path):
    global counter
    print(f"Client connected. Total requests: {counter}")

    try:
        async for message in websocket:
            counter += 1
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")
            print(f"Sent echo back to client: {message}")
    except websockets.ConnectionClosedError:
        print("Client disconnected.")

async def main():
    global counter
    counter = 0
    async with websockets.serve(echo, "localhost", 8765):
        print("Server started and listening on ws://localhost:8765")
        await asyncio.Future()  # รอจนกว่าจะมีการหยุดการทำงาน

asyncio.run(main())
