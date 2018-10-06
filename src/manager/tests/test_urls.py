from django.urls import reverse
from django.test import TestCase


class ManagerURLsTest(TestCase):
    """ Test case for the manager app urls """

    def test_index_url(self):
        """ Test index url """
        self.assertEqual(reverse('manager:index'), '/manager/')

    def test_categories_url(self):
        """ Test categories url """
        self.assertEqual(reverse('manager:categories'), '/manager/categories/')

    def test_category_create_url(self):
        """ Test categories-create url """
        self.assertEqual(
            reverse('manager:category-create'), '/manager/category-create/'
        )

    def test_category_edit_url(self):
        """ Test categories-edit url """
        self.assertEqual(
            reverse('manager:category-edit', args=(1,)),
            '/manager/category-edit/1/'
        )

    def test_category_delete_url(self):
        """ Test categories-delete url """
        self.assertEqual(
            reverse('manager:category-delete', args=(1,)),
            '/manager/category-delete/1/'
        )

    def test_products_url(self):
        """ Test products url """
        self.assertEqual(reverse('manager:products'), '/manager/products/')

    def test_product_create_url(self):
        """ Test product-create url """
        self.assertEqual(
            reverse('manager:product-create'), '/manager/product-create/'
        )

    def test_product_edit_url(self):
        """ Test product-edit url """
        self.assertEqual(
            reverse('manager:product-edit', args=(1,)),
            '/manager/product-edit/1/'
        )

    def test_product_delete_url(self):
        """ Test product-delete url """
        self.assertEqual(
            reverse('manager:product-delete', args=(1,)),
            '/manager/product-delete/1/'
        )
