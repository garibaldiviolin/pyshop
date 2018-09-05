from django.core.management.base import BaseCommand

from website.models import Product, Category


# Create default instances using the app's models

category_list = [
    Category(1, 'Appliances'),
    Category(2, 'Bedroom Furniture')
]

product_list = [
    Product(
        '7891234123459', None, 'Bread toaster', 'Lorem ipsum',
        'bread_toaster.jpg', 35.999, category_list[0].id
    ),
    Product(
        '2012345012349', None, 'Wardrobe', 'Lorem ipsum',
        'wardrobe.jpeg', 55.990, category_list[1].id
    ),
    Product(
        '5901234123457', None, 'Mattress', 'Lorem ipsum',
        'mattress.jpg', 800.724, category_list[1].id
    )
]


class Command(BaseCommand):

    def _create_tags(self):

        Category.objects.all().delete()
        Category.objects.bulk_create(category_list)

        Product.objects.all().delete()
        for product in product_list:
            product.save()

    def handle(self, *args, **options):
        self._create_tags()
