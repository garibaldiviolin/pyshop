from django.db.utils import IntegrityError
from django.test import TestCase

from website.models import Category, Product


class CategoryModelTest(TestCase):
    """ Test case for the Category model """

    description = 'Test123'
    description_update = 'Test321'

    def test_instance(self):
        category = Category(description=self.description)
        self.assertIsInstance(category, Category)

    def test_creation(self):
        created_category = Category.objects.create(
            description=self.description
        )
        queried_category = Category.objects.get(id=created_category.id)
        self.assertEqual(created_category, queried_category)

    def test_str(self):
        expected_result = self.description
        category = Category(description=self.description)
        self.assertEqual(str(category), expected_result)

    def test_repr(self):
        category = Category(description=self.description)
        expected_result = self.description
        self.assertEqual(repr(category), expected_result)


class ProductModelTest(TestCase):
    """ Test case for the Product model """

    category = Category.objects.create(
        description='Category'
    )
    barcode = '5901234123457'
    slug = None
    title = 'Mattress'
    description = 'Mattress'
    image = 'mattress.jpg'
    price = 800.724

    def test_instance(self):
        product = Product(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.pk
        )
        self.assertIsInstance(product, Product)

    def test_creation(self):
        created_product = Product.objects.create(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.id
        )
        queried_product = Product.objects.get(barcode='5901234123457')
        self.assertEqual(created_product, queried_product)

    def test_duplicate_product_creation(self):
        Product.objects.create(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.id
        )
        try:
            Product.objects.create(
                barcode=self.barcode, slug=self.slug, title=self.title,
                description=self.description, image=self.image,
                price=self.price, category_id=self.category.id
            )
            self.fail("IntegrityError UNIQUE constraint error was expected")
        except IntegrityError:
            pass

    def test_str(self):
        expected_result = self.title
        product = Product(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.id
        )
        self.assertEqual(str(product), expected_result)

    def test_repr(self):
        expected_result = self.title
        product = Product(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.id
        )
        self.assertEqual(repr(product), expected_result)
