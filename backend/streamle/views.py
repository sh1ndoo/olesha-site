from rest_framework import viewsets, parsers, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StreamItem
from .serializers import StreamItemSerializer


class RandomStreamView(APIView):
    """
    Возвращает один случайный объект StreamItem.
    """

    def get(self, request, format=None):
        random_stream = StreamItem.objects.order_by('?').first()
        if not random_stream:
            return Response({"detail": "Стримы не найдены."}, status=404)

        serializer = StreamItemSerializer(random_stream)
        return Response(serializer.data)


