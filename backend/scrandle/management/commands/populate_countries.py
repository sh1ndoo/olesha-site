import pycountry
from babel import Locale
from django.core.management.base import BaseCommand
from scrandle.models import Country


class Command(BaseCommand):
    """
    Django-команда для заполнения модели Country списком всех стран мира на русском языке, используя Babel.
    """
    help = 'Populates the database with a list of all countries in Russian using the Babel library.'

    def handle(self, *args, **options):
        if Country.objects.exists():
            self.stdout.write(self.style.WARNING('Countries already exist in the database. Skipping population.'))
            return

        self.stdout.write("Starting to populate countries in Russian using Babel...")

        locale = Locale('ru', 'RU')
        russian_country_names = locale.territories

        countries_to_create = []
        skipped_countries = []

        for country_data in pycountry.countries:
            alpha2_code = country_data.alpha_2
            russian_name = russian_country_names.get(alpha2_code)

            if russian_name:
                countries_to_create.append(Country(name=russian_name))
            else:
                skipped_countries.append(getattr(country_data, 'name', alpha2_code))

        Country.objects.bulk_create(countries_to_create)

        total_countries = len(countries_to_create)
        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with {total_countries} countries.'))

        if skipped_countries:
            skipped_list = ", ".join(skipped_countries)
            self.stdout.write(self.style.NOTICE(
                f'Skipped {len(skipped_countries)} entries not found in Babel locale data: {skipped_list}'))