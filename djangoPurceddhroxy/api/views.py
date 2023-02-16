from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Filter, Packet
from .serializers import FilterSerializer, PacketSerializer


class FiltersListAPI(APIView):
    """
    List of all Filters.
    """
    serializer_class = FilterSerializer

    def get(self, request):
        filters = Filter.objects.all()
        serializer = self.serializer_class(filters, many=True)
        return Response(serializer.data)


class PacketsListAPI(APIView):
    """
    List of all Packets.
    """
    serializer_class = PacketSerializer

    def get(self, request):
        packets = Packet.objects.all()
        serializer = self.serializer_class(packets, many=True)
        return Response(serializer.data)
