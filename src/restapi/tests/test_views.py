import os

from django.urls import reverse
from rest_framework import test, status

from pyshop.settings import BASE_DIR
from website.models import Category, Product


class CategoryViewTest(test.APITransactionTestCase):
    """ Test case for the Category Create view """

    def setUp(self):
        self.category = {
            'description': 'Furniture'
        }

    def test_resource_creation(self):
        """ Test resource (instance) creation in maps endpoint """

        response = self.client.post(
            reverse('restapi:categories'),
            self.category,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)


class ProductViewTest(test.APITransactionTestCase):
    """ Test case for the Product Create view """

    def setUp(self):
        self.category = {
            'description': 'Furniture'
        }
        response_category = self.client.post(
            reverse('restapi:categories'),
            self.category,
            format='json'
        )
        self.category_id = response_category.data['id']

        self.image_path = os.path.join(
            BASE_DIR, 'website/fixtures/', 'sample_image.jpg'
        )
        self.image = open(self.image_path, 'rb')

        self.product = {
            'barcode': '789789789',
            'title': '4654',
            'description': '654',
            'image': self.image,
            'price': '123.000',
            'category': self.category_id
        }

    def test_resource_creation(self):
        """ Test resource (instance) creation in products endpoint """

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'  # has to be multipart because of image field
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

        # remove the image uploaded after tests
        uploaded_image_path = Product.objects.get(
            barcode=self.product['barcode']
        ).image.path
        os.remove(uploaded_image_path)
