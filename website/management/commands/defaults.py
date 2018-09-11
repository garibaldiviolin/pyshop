from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone

from website.models import Product, Category, PurchaseOrder


# Create default instances using the app's models

category_list = [
    Category(1, 'Appliances'),
    Category(2, 'Bedroom Furniture')
]

product_list = [
    Product(
        barcode='7891234123459', slug=None, title='Bread toaster',
        description='Lorem ipsum', image='bread_toaster.jpg', price=35.999,
        category_id=category_list[0].id
    ),
    Product(
        barcode='2012345012349', slug=None, title='Wardrobe',
        description='Lorem ipsum', image='wardrobe.jpeg', price=55.990,
        category_id=category_list[1].id
    ),
    Product(
        barcode='5901234123457', slug=None, title='Mattress',
        description='Lorem ipsum', image='mattress.jpg', price=800.724,
        category_id=category_list[1].id
    )
]

user = User.objects.first()

purchase_order_list = [
    PurchaseOrder(timestamp=timezone.now(), user=user, cart=False),
    PurchaseOrder(timestamp=timezone.now(), user=user, cart=False),
    PurchaseOrder(timestamp=timezone.now(), user=user, cart=False),
]


class Command(BaseCommand):

    def _create_tags(self):

        Category.objects.all().delete()
        Category.objects.bulk_create(category_list)

        Product.objects.all().delete()
        for product in product_list:
            product.save()

        PurchaseOrder.objects.all().delete()
        PurchaseOrder.objects.bulk_create(purchase_order_list)

    def handle(self, *args, **options):
        self._create_tags()
