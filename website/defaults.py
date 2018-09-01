from .models import Product

# Create default instances using the app's models

product_list = [
    Product(
        '7891234123459', 'Bread toaster', 'Lorem ipsum',
        'bread_toaster.jpg', 35.999
    ),
    Product(
        '2012345012349', 'Wardrobe', 'Lorem ipsum',
        'wardrobe.jpeg', 55.990
    ),
    Product(
        '5901234123457', 'Mattress', 'Lorem ipsum',
        'mattress.jpg', 800.724
    )
]


def create_default_products():
    Product.objects.all().delete()
    Product.objects.bulk_create(product_list)
