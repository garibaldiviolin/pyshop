""" This module tests website app urls """

from django.urls import reverse
from django.test import TestCase


class WebsiteURLsTest(TestCase):
    """ Test case for the website app urls """

    def test_index_url(self):
        """ Test index url """
        self.assertEqual(reverse('website:index'), '/')

    def test_signin_url(self):
        """ Test signin url """
        self.assertEqual(reverse('website:signin'), '/signin/')

    def test_signout_url(self):
        """ Test signout url """
        self.assertEqual(reverse('website:signout'), '/signout/')

    def test_signup_url(self):
        """ Test signup url """
        self.assertEqual(reverse('website:signup'), '/signup/')

    def test_purchase_orders_url(self):
        """ Test purchase-orders url """
        self.assertEqual(
            reverse('website:purchase-orders'), '/purchase-orders/'
        )

    def test_purchase_order_url(self):
        """ Test purchase-order/pk/ url """
        self.assertEqual(
            reverse('website:purchase-order', args=(1,)), '/purchase-order/1/'
        )

    def test_complete_purchase_order_url(self):
        """ Test complete-purchase-order/pk/ url """
        self.assertEqual(
            reverse('website:complete-purchase-order', args=(1,)),
            '/complete-purchase-order/1/'
        )

    def test_profile_url(self):
        """ Test profile url """
        self.assertEqual(reverse('website:profile'), '/profile/')

    def test_product_detail_url(self):
        """ Test products/pk/ url """
        self.assertEqual(
            reverse('website:product-detail', args=(1,)), '/products/1/'
        )

    def test_add_to_cart_url(self):
        """ Test add-to-cart/pk/ url """
        self.assertEqual(reverse('website:add-to-cart'), '/add-to-cart/')
