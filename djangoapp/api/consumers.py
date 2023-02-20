import json
from channels.generic.websocket import AsyncWebsocketConsumer
from scapy.layers.l2 import Ether

from .models import Packet
from .serializers import PacketSerializer


class PacketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Parse packet from text_data
        ether = Ether(text_data)
        print("MERDA A PALATE")
        print(ether)
        # Save packet to database as Django model object
        pkt_data = PacketSerializer.process_packet(ether)
        pkt_obj = Packet.objects.create(**pkt_data)

        # Send the packet to the Django server and receive the response
        await self.send(text_data=json.dumps(pkt_obj))
