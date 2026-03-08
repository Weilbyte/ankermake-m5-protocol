import asyncio
import websockets
import json

async def test():
    uri = "ws://127.0.0.1:4470/ws/ctrl"
    async with websockets.connect(uri) as websocket:
        gcode_multi = "M140 S0\nM104 S0\n"
        payload = {
            "mqtt": {
                "commandType": 1043,
                "cmdData": gcode_multi,
                "cmdLen": len(gcode_multi)
            }
        }
        await websocket.send(json.dumps(payload))
        print("Set Nozzle Temperature 220")
        
        # Keep connection open to read backend ACK
        while True:
            response = await websocket.recv()
            print(f"Server response: {response}")

asyncio.run(test())
