#!/usr/bin/env python3
import asyncio
import websockets
import time
import random


# --- New function to set a random color ---
async def set_random_color(websocket):
    """Generates more distinct random colors."""
    # Use the full hue range but with more strategic saturation/value
    hue = random.randint(0, 255)

    # Create distinct groups of colors
    color_type = random.choice(['vibrant', 'bright', 'muted'])

    if color_type == 'vibrant':
        saturation = random.randint(200, 255)
        value = random.randint(220, 255)
    elif color_type == 'bright':
        saturation = random.randint(150, 220)
        value = random.randint(200, 255)
    else:  # muted
        saturation = random.randint(100, 180)
        value = random.randint(150, 220)

    print(f"\n--- {color_type} color: H:{hue}, S:{saturation}, V:{value} ---")
    await websocket.send(f"9:2:led_hue:{hue}")
    await websocket.send(f"9:2:led_saturation:{saturation}")
    # await websocket.send(f"9:2:led_value:{value}")
    # await asyncio.sleep(0.1)


# --- Main connection and control function ---
async def control_device():
    uri = "ws://akclock.local/ws"

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to the device.")
                await mimic_screensaver_sequence(websocket)
                await set_display_mode(websocket, 2)
                await set_random_color(websocket)
                await asyncio.sleep(1)
                await set_random_color(websocket)
                await asyncio.sleep(1)

                await set_display_mode(websocket, 1)
                await set_random_color(websocket)
                await asyncio.sleep(1)
                await set_random_color(websocket)
                await asyncio.sleep(1)

                await mimic_screensaver_sequence(websocket)
                await set_display_mode(websocket, 0)
                await set_random_color(websocket)
                await asyncio.sleep(2)
                await set_random_color(websocket)

        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Connection closed unexpectedly: {e}")
            print("Retrying connection in 5 seconds...")
            await asyncio.sleep(5)  # Wait before attempting to reconnect
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying connection in 5 seconds...")
            await asyncio.sleep(5)

async def set_display_mode(websocket, mode):
    message = f"9:1:time_or_date:{mode}"
    await websocket.send(message)
    print(f"Sent: {message} - Changed display mode to {mode}.")
    await asyncio.sleep(1)


async def mimic_screensaver_sequence(websocket):
    print("\n--- Starting screen saver sequence ---")
    await websocket.send("9:1:display_on:1")
    await asyncio.sleep(0.1)

    await websocket.send("9:1:display_off:3")
    await asyncio.sleep(2)

    await websocket.send("9:1:display_on:1")
    await asyncio.sleep(0.1)

    await websocket.send("9:1:display_off:24")

    print("--- Screen saver sequence finished. ---")


if __name__ == "__main__":
    asyncio.run(control_device())
