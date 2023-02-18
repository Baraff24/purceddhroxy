from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import Filter, Packet
from .serializers import FilterSerializer, PacketSerializer


class FiltersListAPI(generics.ListAPIView):
    """
    List of all Filters.
    """
    permission_classes = [IsAdminUser]
    serializer_class = FilterSerializer
    queryset = Filter.objects.all()
    search_fields = ['name', 'function', 'is_active']

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class FilterDetailAPI(APIView):
    """
    Detail of a Filter.
    """
    serializer_class = FilterSerializer

    def get(self, request, pk):
        obj = Filter.objects.get(pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = Filter.objects.get(pk=pk)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @staticmethod
    def delete(request, pk):
        obj = Filter.objects.get(pk=pk)
        obj.is_active = False
        return Response({"message": "Filter deactivated successfully."})


class PacketsListAPI(generics.ListAPIView):
    """
    List of all Packets.
    """
    permission_classes = [IsAdminUser]
    serializer_class = PacketSerializer
    queryset = Packet.objects.all()
    search_fields = ['src_ip', 'dst_ip', 'payload', 'dangerous', 'created_at']
