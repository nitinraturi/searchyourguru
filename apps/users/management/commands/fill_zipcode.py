from django.core.management.base import BaseCommand
from apps.users.utils import fetch_zipcode_from_api, fetch_zipcodes_from_excel_file


class Command(BaseCommand):
    help = 'Fetch zipcode data from API'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='excel file path containing zipcodes')

    def handle(self, *args, **options):
        if fetch_zipcodes_from_excel_file(options['path']):
            self.stdout.write('Database has populated with zipcode data')
        else:
            self.stderr.write('Internal error encountered')


