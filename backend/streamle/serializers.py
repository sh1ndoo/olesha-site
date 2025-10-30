from rest_framework import serializers
from .models import StreamItem, Game



class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['image', 'title']

class StreamItemSerializer(serializers.ModelSerializer):
    games_played = GameSerializer(many=True, read_only=True)

    class Meta:
        model = StreamItem
        fields = '__all__'


# class StreamleItemSerializer(serializers.ModelSerializer):
#     # Используем PrimaryKeyRelatedField для получения ID тегов при создании/обновлении
#     stream = serializers.PrimaryKeyRelatedField(
#         queryset=StreamItem.objects.all(),
#         many=True
#     )
#
#     class Meta:
#         model = StreamleItem
#         fields = '__all__'
#         read_only_fields = ('id',)