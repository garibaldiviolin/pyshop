from django.test import TestCase
from django.urls import reverse

from website.models import Category, Product


class ProductsViewTest(TestCase):
    """ Test case for the ProductsView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        Product.objects.create(
            barcode='5901234123457', title='Mattress',
            description='Mattress', image='mattress.jpg', price=800.724,
            category=self.category
        )
        self.product_queryset = Product.objects.all()
        self.category_queryset = Category.objects.all()

    def test_list_products(self):
        response = self.client.get(reverse('website:index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context_data['product_list']),
            list(self.product_queryset)
        )
        self.assertEqual(
            list(response.context_data['categories']),
            list(self.category_queryset)
        )
