import json
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from streamle.models import StreamItem, Game  # <-- Замените 'your_app_name' на имя вашего приложения


class Command(BaseCommand):
    help = 'Импортирует данные о стримах из JSON файла в базу данных'

    def add_arguments(self, parser):
        # Добавляем аргумент для указания пути к JSON файлу
        parser.add_argument('json_file', type=str, help='Путь к JSON файлу с данными о стримах')

    def handle(self, *args, **options):
        # Получаем путь к файлу из аргументов команды
        json_file_path = options['json_file']

        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Файл не найден по пути: {json_file_path}'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Ошибка декодирования JSON. Проверьте формат файла.'))
            return

        # Счетчик для статистики
        created_streams_count = 0

        for item in data:
            stream_id = item.get('streamId')
            if not stream_id:
                self.stdout.write(self.style.WARNING('Пропущен элемент без streamId'))
                continue

            # Проверяем, существует ли уже стрим с таким ID, чтобы избежать дублей
            if StreamItem.objects.filter(id_stream=stream_id).exists():
                self.stdout.write(self.style.NOTICE(f'Стрим с ID {stream_id} уже существует. Пропускаем.'))
                continue

            # 1. Парсим строку с играми
            # Формат: "Название1|slug1|URL1|Название2|slug2|URL2|..."
            games_played_str = item.get('gamesplayed', '')
            games_data = games_played_str.split('|')

            # Мы ожидаем, что на каждую игру приходится 3 элемента (название, slug, URL)
            games_to_add = []
            if len(games_data) >= 3:
                for i in range(0, len(games_data), 3):
                    game_title = games_data[i]
                    # Проверяем, есть ли slug и URL
                    if i + 2 < len(games_data):
                        game_image_url = games_data[i + 2]

                        # 2. Находим или создаем объект Game
                        # get_or_create возвращает кортеж (объект, был_ли_он_создан)
                        game, created = Game.objects.get_or_create(
                            title=game_title,
                            defaults={'image': game_image_url}
                        )
                        if created:
                            self.stdout.write(self.style.SUCCESS(f'Создана новая игра: "{game.title}"'))
                        games_to_add.append(game)

            # 3. Создаем объект StreamItem
            try:
                stream_date = parse_datetime(item['starttime'])

                stream = StreamItem.objects.create(
                    id_stream=stream_id,
                    title=item.get('title', 'Без названия'),
                    avg_viewers=item.get('avgviewers', 0),
                    max_viewers=item.get('maxviewers', 0),
                    date=stream_date,
                    length=item.get('length', 0),
                    view_minutes=item.get('viewminutes', 0),
                    follower_gain=item.get('followergain', 0)
                )

                # 4. Добавляем связь Many-to-Many с играми
                if games_to_add:
                    stream.games_played.set(games_to_add)

                created_streams_count += 1
                self.stdout.write(self.style.SUCCESS(f'Успешно импортирован стрим с ID: {stream_id}'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Ошибка при создании стрима {stream_id}: {e}'))

        self.stdout.write(
            self.style.SUCCESS(f'\nИмпорт завершен. Всего создано {created_streams_count} новых записей о стримах.'))