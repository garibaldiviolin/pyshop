from .models import Product, Category


# Create default instances using the app's models

category_list = [
    Category(1, 'Appliances'),
    Category(2, 'Bedroom Furniture')
]

product_list = [
    Product(
        '7891234123459', 'Bread toaster', 'Lorem ipsum',
        'bread_toaster.jpg', 35.999, category_list[0].id
    ),
    Product(
        '2012345012349', 'Wardrobe', 'Lorem ipsum',
        'wardrobe.jpeg', 55.990, category_list[1].id
    ),
    Product(
        '5901234123457', 'Mattress', 'Lorem ipsum',
        'mattress.jpg', 800.724, category_list[1].id
    )
]


def create_default_database_instances():

    Category.objects.all().delete()
    Category.objects.bulk_create(category_list)

    Product.objects.all().delete()
    Product.objects.bulk_create(product_list)
