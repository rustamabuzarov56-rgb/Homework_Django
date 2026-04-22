from django.core.management import call_command
from django.core.management.base import BaseCommand
from unicodedata import category

from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        try:
            call_command("loaddata", "catalog-fixture.json")
            self.stdout.write(self.style.SUCCESS(f"Данные успешно загружены из фикстур!"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Ошибка при загрузке фикстур: {e}"))