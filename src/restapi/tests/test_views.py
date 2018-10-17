""" This module tests restapi app views """

import os

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import test, status

from pyshop.settings import BASE_DIR
from website.models import Category, Product, PaymentMethod, PurchaseOrder


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

    def test_blank_description(self):
        """ Test resource (instance) creation with blank description """

        self.category.update({'description': ''})

        response = self.client.post(
            reverse('restapi:categories'),
            self.category,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PaymentMethod.objects.count(), 0)

    def test_without_description(self):
        """ Test resource (instance) creation without description """

        del self.category['description']

        response = self.client.post(
            reverse('restapi:categories'),
            self.category,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PaymentMethod.objects.count(), 0)


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

    def remove_uploaded_image(self, barcode):
        ''' Remove the image uploaded after tests '''

        uploaded_image_path = Product.objects.get(
            barcode=barcode
        ).image.path
        os.remove(uploaded_image_path)

    def test_resource_creation(self):
        """ Test resource (instance) creation in products endpoint """

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'  # has to be multipart because of image field
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

        self.remove_uploaded_image(self.product['barcode'])

    def test_blank_barcode(self):
        """ Test resource (instance) creation with blank barcode """

        self.product.update({'barcode': ''})

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_without_barcode(self):
        """ Test resource (instance) creation without barcode """

        del self.product['barcode']

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_duplicated_barcode(self):
        """ Test duplicated resource (instance) creation """

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

        self.remove_uploaded_image(self.product['barcode'])

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 1)

    def test_blank_title(self):
        """ Test resource (instance) creation with blank title """

        self.product.update({'title': ''})

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_without_title(self):
        """ Test resource (instance) creation without title """

        del self.product['title']

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_blank_description(self):
        """ Test resource (instance) creation with blank description """

        self.product.update({'description': ''})

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_without_description(self):
        """ Test resource (instance) creation without description """

        del self.product['description']

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_blank_image(self):
        """ Test resource (instance) creation with blank image """

        self.product.update({'image': ''})

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_without_image(self):
        """ Test resource (instance) creation without image """

        del self.product['image']

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_blank_price(self):
        """ Test resource (instance) creation with blank price """

        self.product.update({'price': ''})

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_invalid_price(self):
        """ Test resource (instance) creation with invalid price """

        self.product.update({'price': 'A'})  # 'A' is invalid

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_without_price(self):
        """ Test resource (instance) creation without price """

        del self.product['price']

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_blank_category(self):
        """ Test resource (instance) creation with blank category """

        self.product.update({'category': ''})

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)

    def test_without_category(self):
        """ Test resource (instance) creation without category """

        del self.product['category']

        response = self.client.post(
            reverse('restapi:products'),
            self.product,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 0)


class PaymentMethodCreateViewTest(test.APITransactionTestCase):
    """ Test case for the PaymentMethod CreateAPIView """

    def setUp(self):
        self.payment_method = {
            'description': 'Cash'
        }

    def test_resource_creation(self):
        """ Test resource (instance) creation in maps endpoint """

        response = self.client.post(
            reverse('restapi:payment-methods'),
            self.payment_method,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PaymentMethod.objects.count(), 1)

    def test_blank_description(self):
        """ Test resource (instance) creation with blank description """

        self.payment_method.update({'description': ''})

        response = self.client.post(
            reverse('restapi:payment-methods'),
            self.payment_method,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PaymentMethod.objects.count(), 0)

    def test_without_description(self):
        """ Test resource (instance) creation without description """

        del self.payment_method['description']

        response = self.client.post(
            reverse('restapi:payment-methods'),
            self.payment_method,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PaymentMethod.objects.count(), 0)


class PurchaseOrderViewTest(test.APITransactionTestCase):
    """ Test case for the PurchaseOrder Create view """

    def setUp(self):
        self.user = User.objects.get_or_create(username='testuser')[0]

        self.purchase_order = {
            "id": 1,
            "timestamp": "2018-10-09T01:15:00Z",
            "cart": True,
            "user": self.user.id
        }

    def test_resource_creation(self):
        """ Test resource (instance) creation in products endpoint """

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)

    def test_blank_timestamp(self):
        """ Test resource (instance) creation with blank timestamp """

        self.purchase_order.update({'timestamp': ''})

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_invalid_timestamp(self):
        """ Test resource (instance) creation with invalid timestamp """

        self.purchase_order.update({'timestamp': 'AAA'})

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_without_timestamp(self):
        """ Test resource (instance) creation without timestamp """

        del self.purchase_order['timestamp']

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_blank_cart(self):
        """ Test resource (instance) creation with blank cart """

        self.purchase_order.update({'cart': ''})

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_invalid_cart(self):
        """ Test resource (instance) creation with invalid cart """

        self.purchase_order.update({'cart': 'AAA'})

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_without_cart(self):
        """ Test resource (instance) creation without cart """

        del self.purchase_order['cart']

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_blank_user(self):
        """ Test resource (instance) creation with blank user """

        self.purchase_order.update({'user': ''})

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_invalid_user(self):
        """ Test resource (instance) creation with invalid user """

        self.purchase_order.update({'user': 5})

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)

    def test_without_user(self):
        """ Test resource (instance) creation without user """

        del self.purchase_order['user']

        response = self.client.post(
            reverse('restapi:purchase-orders'),
            self.purchase_order,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 0)
