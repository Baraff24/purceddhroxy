from rest_framework import serializers
from scapy.layers.l2 import Ether

from .models import Filter, Packet


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'


class PacketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    src_ip = serializers.CharField(max_length=17)
    dst_ip = serializers.CharField(max_length=17)
    type = serializers.CharField(max_length=5)
    payload = serializers.CharField()

    @staticmethod
    def process_packet(ether):
        if ether:
            return {
                'src_ip': ether.dst,
                'dst_ip': ether.src,
                'type': hex(ether.type),
                'payload': str(ether.payload)
            }
        else:
            return None

    def create(self, validated_data):
        return Packet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass
