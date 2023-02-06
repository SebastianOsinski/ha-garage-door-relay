from lcus_relay import Relay
import asyncio


class GarageRemote:
    def __init__(self, serial_port, press_time):
        self._relay = Relay(serial_port)
        self._press_time = press_time

    async def press(self):
        self._relay.turn_on()

        await asyncio.sleep(self._press_time)

        self._relay.turn_off()
