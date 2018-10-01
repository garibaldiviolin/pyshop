from django.urls import reverse
from django.test import TestCase


class WebsiteURLsTest(TestCase):
    """ Test case for the website app urls """

    def test_index_url(self):
        self.assertEqual(reverse('website:index'), '/')

    def test_signin_url(self):
        self.assertEqual(reverse('website:signin'), '/signin/')

    def test_signout_url(self):
        self.assertEqual(reverse('website:signout'), '/signout/')

    def test_signup_url(self):
        self.assertEqual(reverse('website:signup'), '/signup/')

    def test_purchase_orders_url(self):
        self.assertEqual(
            reverse('website:purchase-orders'), '/purchase-orders/'
        )

    def test_purchase_order_url(self):
        self.assertEqual(
            reverse('website:purchase-order', args=(1,)), '/purchase-order/1/'
        )

    def test_complete_purchase_order_url(self):
        self.assertEqual(
            reverse('website:complete-purchase-order', args=(1,)),
            '/complete-purchase-order/1/'
        )

    def test_profile_url(self):
        self.assertEqual(reverse('website:profile'), '/profile/')

    def test_product_detail_url(self):
        self.assertEqual(
            reverse('website:product-detail', args=(1,)), '/products/1/'
        )

    def test_add_to_cart_url(self):
        self.assertEqual(reverse('website:add-to-cart'), '/add-to-cart/')
