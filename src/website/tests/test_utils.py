""" This module tests website app util methods """

from django.test import TestCase

from website.models import Category, Product
from website.utils import unique_slug_generator


class UniqueSlugGeneratorTest(TestCase):
    """ Test case for unique_slug_generator method """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

    def test_slug(self):
        expected_result = 'new-mattress'
        product = Product(
            barcode='5901234123457', title='New Mattress',
            description='Mattress', image='mattress.jpg',
            price=800.724, category=self.category
        )
        slug = unique_slug_generator(product)
        self.assertEqual(slug, expected_result)
