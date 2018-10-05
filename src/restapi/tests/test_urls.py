from django.urls import reverse
from django.test import TestCase


class RESTAPIURLsTest(TestCase):
    """ Test case for the restapi app urls """

    def test_categories_url(self):
        self.assertEqual(reverse('restapi:categories'), '/api/v1/categories/')

    def test_products_url(self):
        self.assertEqual(reverse('restapi:products'), '/api/v1/products/')

    def test_payment_methods_url(self):
        self.assertEqual(
            reverse('restapi:payment-methods'),
            '/api/v1/payment-methods/'
        )
