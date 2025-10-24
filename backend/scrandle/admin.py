from django.contrib import admin
from .models import ScranItem, Country, Tag

from django.contrib import admin, messages
from django.utils.html import mark_safe


@admin.register(ScranItem)
class ScranItemAdmin(admin.ModelAdmin):
    """
    Класс для кастомизации отображения модели ScranItem в админ-панели Django.
    """

    # Поля, которые будут отображаться в списке объектов
    list_display = ('image_preview', 'name', 'description', 'price', 'place', 'is_moderated')

    # Поля, которые будут ссылками на страницу редактирования объекта
    list_display_links = ('image_preview', 'name')

    # Добавляем возможность поиска по текстовым полям
    search_fields = ('name', 'description', 'place')

    # Добавляем фильтрацию по статусу модерации и стране
    list_filter = ('is_moderated', 'country')

    # Добавляем наши кастомные действия
    actions = ['make_moderated', 'make_unmoderated']

    def image_preview(self, obj):
        """
        Метод для отображения миниатюры изображения в списке.
        """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height: 60px;">')
        return "Нет изображения"

    image_preview.short_description = 'Изображение'

    @admin.action(description="Одобрить выбранные (is_moderated = True)")
    def make_moderated(self, request, queryset):
        """
        Действие для установки флага is_moderated в True для выбранных объектов.
        """
        # .update() - это эффективный способ обновить много записей одним запросом
        updated_count = queryset.update(is_moderated=True)
        # Сообщение для пользователя о результате
        self.message_user(
            request,
            f"{updated_count} записей было успешно одобрено.",
            messages.SUCCESS
        )

    @admin.action(description="Отклонить/Снять с публикации (is_moderated = False)")
    def make_unmoderated(self, request, queryset):
        """
        Действие для установки флага is_moderated в False для выбранных объектов.
        """
        updated_count = queryset.update(is_moderated=False)
        self.message_user(
            request,
            f"{updated_count} записей было отмечено как не прошедшие модерацию.",
            messages.SUCCESS
        )
admin.site.register(Country)
admin.site.register(Tag)