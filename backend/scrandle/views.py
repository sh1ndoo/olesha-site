from rest_framework import generics, parsers, viewsets, status
from rest_framework.response import Response

from .models import ScranItem, Tag, Country
from .serializers import ScranItemSerializer, CountrySerializer, TagSerializer


class TagListView(generics.ListAPIView):
    """
    Представление для получения списка всех тегов.
    """
    queryset = Tag.objects.order_by('name')
    serializer_class = TagSerializer


class CountryListView(generics.ListAPIView):
    """
    Представление для получения списка всех стран.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ScranViewSet(viewsets.ModelViewSet):
    """
    ViewSet для создания, получения, обновления и удаления "скранов".
    """
    queryset = ScranItem.objects.filter(is_moderated=True)  # Показываем только одобренные
    serializer_class = ScranItemSerializer
    # Добавляем MultiPartParser для обработки загрузки файлов
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)

    def create(self, request, *args, **kwargs):
        # Преобразуем строковые названия тегов и страны в их ID
        mutable_data = request.data.copy()

        # Обработка тегов
        tag_names = mutable_data.getlist('tags')
        tag_ids = []
        for name in tag_names:
            # Создаем тег, если его нет
            tag, created = Tag.objects.get_or_create(name=name)
            tag_ids.append(tag.id)
        mutable_data.setlist('tags', tag_ids)

        # Обработка страны
        country_name = mutable_data.get('country[name]')  # Vue-multiselect может отправлять объект
        if not country_name:
            country_name = mutable_data.get('country')
        if country_name:
            # Создаем страну, если ее нет
            country, created = Country.objects.get_or_create(name=country_name)
            mutable_data['country'] = country.id

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




# class ScranCoupleGetView(generics.ListAPIView):
#     queryset = ScranCouple.objects.all()
#     serializer_class = ScranCoupleSerializer



