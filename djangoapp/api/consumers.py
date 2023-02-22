from channels.generic.websocket import AsyncWebsocketConsumer
from scapy.layers.l2 import Ether

from .functions import parse_packet


class PacketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Parse packet from text_data
        packet = Ether(text_data)

        # Parse packet and return serialized packet
        serialized_packet = parse_packet(packet)

        # Send serialized packet to the client
        await self.send(text_data=serialized_packet)


