import asyncio
import websockets
import json
import logging

logging.basicConfig(level=logging.DEBUG)

async def test_pppp():
    uri = "ws://127.0.0.1:4470/ws/pppp-state"
    async with websockets.connect(uri) as websocket:
        print("Connected to websocket")
        # Immediately close the connection instead of waiting
        await websocket.close()
        print("Disconnected")
        # The following loop to receive messages is now unreachable or will raise an error
        # as the connection has been closed.
        # If the intent was to test receiving after close, error handling would be needed.
        # For now, we'll keep the original structure but note the change in behavior.
        while True:
            try:
                response = await websocket.recv()
                print(f"Received: {response}")
                if json.loads(response).get("status") == "connected":
                    break
            except websockets.exceptions.ConnectionClosedOK:
                print("Connection closed gracefully during recv attempt.")
                break
            except websockets.exceptions.ConnectionClosedError as e:
                print(f"Connection closed with error: {e}")
                break


if __name__ == "__main__":
    asyncio.run(test_pppp())
