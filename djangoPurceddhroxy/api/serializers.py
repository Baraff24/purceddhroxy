from rest_framework import serializers

from .models import Filter, Packet


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'


class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = '__all__'
