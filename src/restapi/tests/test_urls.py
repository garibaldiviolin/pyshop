""" This module tests restapi app urls """

from django.urls import reverse
from django.test import TestCase


class RESTAPIURLsTest(TestCase):
    """ Test case for the restapi app urls """

    def test_categories_url(self):
        """ Test categories url """
        self.assertEqual(reverse('restapi:categories'), '/api/v1/categories/')

    def test_products_url(self):
        """ Test products url """
        self.assertEqual(reverse('restapi:products'), '/api/v1/products/')

    def test_payment_methods_url(self):
        """ Test payment-methods url """
        self.assertEqual(
            reverse('restapi:payment-methods'),
            '/api/v1/payment-methods/'
        )

    def test_purchase_orders_url(self):
        """ Test purchase orders url """
        self.assertEqual(
            reverse('restapi:purchase-orders'),
            '/api/v1/purchase-orders/'
        )
