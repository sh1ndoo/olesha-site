from rest_framework import serializers
from .models import ScranItem

# your_app/serializers.py

from rest_framework import serializers
from .models import ScranItem, Tag, Country

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class ScranItemSerializer(serializers.ModelSerializer):
    # Используем PrimaryKeyRelatedField для получения ID тегов при создании/обновлении
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all()
    )

    class Meta:
        model = ScranItem
        fields = (
            'id',
            'name',
            'description',
            'image',
            'place',
            'country',
            'year',
            'price',
            'tags'
        )
        # Поля, которые можно только читать и которые будут включены в ответ
        read_only_fields = ('id',)

    def to_representation(self, instance):
        """
        Переопределяем, чтобы в ответе вместо ID тегов и страны
        были их полные данные (объекты).
        """
        representation = super().to_representation(instance)
        representation['tags'] = TagSerializer(instance.tags.all(), many=True).data
        representation['country'] = CountrySerializer(instance.country).data
        return representation

    def create(self, validated_data):
        """
        Переопределяем метод create для обработки ManyToMany поля 'tags'.
        """
        tags_data = validated_data.pop('tags')
        scran = ScranItem.objects.create(**validated_data)
        scran.tags.set(tags_data)
        return scran



#
# class ScranCoupleSerializer(serializers.ModelSerializer):
#     items = ScranItemSerializer(many=True)
#
#     class Meta:
#         model = ScranCouple
#         fields = (
#             "scran1",
#             "scran2",
#         )