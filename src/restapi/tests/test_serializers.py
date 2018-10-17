""" This module tests restapi app serializers """

import os
from shutil import copyfile

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import serializers

from pyshop.settings import BASE_DIR
from website.models import (
    Category,
    Product,
    PaymentMethod,
    PurchaseOrder,
    PurchaseItem
)
from ..serializers import (
    CategorySerializer,
    ProductSerializer,
    PaymentMethodSerializer,
    PurchaseOrderSerializer,
    PurchaseItemSerializer,
)


class CategorySerializerTest(TestCase):
    """ Test case for the Category model serializer """

    def setUp(self):
        self.category = Category(description='Furnitures')
        self.serializer = CategorySerializer(instance=self.category)
        self.json = {
            'description': '',
        }

    def test_description_content(self):
        """ Test description field value """

        self.assertEqual(
            self.category.description,
            self.serializer.data['description']
        )

    def test_blank_description(self):
        """ Test blank description field value """

        serializer = CategorySerializer(data=self.json)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('description', serializer.errors.keys())
        self.assertIn('blank', str(serializer.errors.values()))


class ProductSerializerTest(TestCase):
    """ Test case for the Product model serializer """

    def setUp(self):
        self.image_path = os.path.join(
            BASE_DIR, 'website/fixtures/', 'sample_image.jpg'
        )
        self.image = open(self.image_path, 'rb')

        self.json = {
            'barcode': '789789789',
            'title': '4654',
            'description': '654',
            'image': self.image,
            'price': '123.000',
            'category': 1
        }

        self.category = Category.objects.create(description='Furnitures')

        self.product = Product(
            barcode='789789789',
            title='Mattress',
            description='Sleep Mattress',
            image=self.image,
            price=123.000,
            category=self.category
        )
        self.serializer = ProductSerializer(
            instance=self.product
        )

    def test_barcode_content(self):
        """ Test barcode field value """

        self.assertEqual(
            self.product.barcode,
            self.serializer.data['barcode']
        )

    def test_title_content(self):
        """ Test title field value """

        self.assertEqual(
            self.product.title,
            self.serializer.data['title']
        )

    def test_description_content(self):
        """ Test description field value """

        self.assertEqual(
            self.product.description,
            self.serializer.data['description']
        )

    def test_price_content(self):
        """ Test price field value """

        self.assertEqual(
            self.product.price,
            float(self.serializer.data['price'])
        )

    def test_category_content(self):
        """ Test category id field value """

        self.assertEqual(
            self.product.category.id,
            self.serializer.data['category']
        )

    def test_blank_barcode(self):
        """ Test using blank barcode value """

        data = self.json
        data.update({'barcode': ''})
        exception_serializer = ProductSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('barcode', exception_serializer.errors.keys())
        self.assertIn('blank', str(exception_serializer.errors.values()))

    def test_blank_title(self):
        """ Test using blank title value """

        data = self.json
        data.update({'title': ''})
        exception_serializer = ProductSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('title', exception_serializer.errors.keys())
        self.assertIn('blank', str(exception_serializer.errors.values()))

    def test_blank_description(self):
        """ Test using blank description value """

        data = self.json
        data.update({'description': ''})
        exception_serializer = ProductSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('description', exception_serializer.errors.keys())
        self.assertIn('blank', str(exception_serializer.errors.values()))

    def test_blank_image(self):
        """ Test using blank image value """

        data = self.json
        data.update({'image': ''})
        exception_serializer = ProductSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('image', exception_serializer.errors.keys())
        self.assertIn(
            'The submitted data was not a file',
            str(exception_serializer.errors.values())
        )

    def test_blank_price(self):
        """ Test using blank price value """

        data = self.json
        data.update({'price': ''})
        exception_serializer = ProductSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('price', exception_serializer.errors.keys())
        self.assertIn(
            'valid number', str(exception_serializer.errors.values())
        )

    def test_null_category(self):
        """ Test using null category id value """

        data = self.json
        data.update({'category': ''})
        exception_serializer = ProductSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('category', exception_serializer.errors.keys())
        self.assertIn('null', str(exception_serializer.errors.values()))


class PaymentMethodSerializerTest(TestCase):
    """ Test case for the PaymentMethod model serializer """

    def setUp(self):
        self.payment_method = PaymentMethod(description='Cash')
        self.serializer = PaymentMethodSerializer(instance=self.payment_method)
        self.json = {
            'description': '',
        }

    def test_description_content(self):
        """ Test description field value """

        self.assertEqual(
            self.payment_method.description,
            self.serializer.data['description']
        )

    def test_blank_description(self):
        """ Test blank description field value """

        serializer = PaymentMethodSerializer(data=self.json)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('description', serializer.errors.keys())
        self.assertIn('blank', str(serializer.errors.values()))


class PurchaseOrderSerializerTest(TestCase):
    """ Test case for the PurchaseOrder model serializer """

    def setUp(self):
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.purchase_order = PurchaseOrder.objects.create(
            timestamp='2018-10-09T01:15:00Z', user=self.user, cart=False
        )
        self.serializer = PurchaseOrderSerializer(instance=self.purchase_order)
        self.json = {
            'id': 1,
            'timestamp': '2018-10-09T01:15:00Z',
            'cart': True,
            'user': self.user.id
        }

    def test_id_content(self):
        """ Test id field value """

        self.assertEqual(
            self.purchase_order.id,
            self.serializer.data['id']
        )

    def test_timestamp_content(self):
        """ Test timestamp field value """

        self.assertEqual(
            self.purchase_order.timestamp,
            self.serializer.data['timestamp']
        )

    def test_invalid_timestamp(self):
        """ Test invalid timestamp field value """

        data = self.json
        data.update({'timestamp': 'AA'})
        serializer = PurchaseOrderSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('timestamp', serializer.errors.keys())
        self.assertIn(
            'Datetime has wrong format.',
            str(serializer.errors.values())
        )

    def test_blank_timestamp(self):
        """ Test blank timestamp field value """

        data = self.json
        data.update({'timestamp': ''})
        serializer = PurchaseOrderSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('timestamp', serializer.errors.keys())
        self.assertIn(
            'Datetime has wrong format.',
            str(serializer.errors.values())
        )

    def test_cart_content(self):
        """ Test cart field value """

        self.assertEqual(
            self.purchase_order.cart,
            self.serializer.data['cart']
        )

    def test_invalid_cart(self):
        """ Test invalid cart field value """

        data = self.json
        data.update({'cart': 'AA'})
        serializer = PurchaseOrderSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('cart', serializer.errors.keys())
        self.assertIn(
            'is not a valid boolean.',
            str(serializer.errors.values())
        )

    def test_blank_cart(self):
        """ Test blank cart field value """

        data = self.json
        data.update({'cart': ''})
        serializer = PurchaseOrderSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('cart', serializer.errors.keys())
        self.assertIn(
            'is not a valid boolean.',
            str(serializer.errors.values())
        )

    def test_user_content(self):
        """ Test user field value """

        self.assertEqual(
            self.purchase_order.user.id,
            self.serializer.data['user']
        )

    def test_invalid_user(self):
        """ Test invalid user field value """

        data = self.json
        data.update({'user': 12})
        serializer = PurchaseOrderSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('user', serializer.errors.keys())
        self.assertIn(
            'Invalid pk',
            str(serializer.errors.values())
        )

    def test_blank_user(self):
        """ Test blank user field value """

        data = self.json
        data.update({'user': ''})
        serializer = PurchaseOrderSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('user', serializer.errors.keys())
        self.assertIn(
            'null',
            str(serializer.errors.values())
        )


class PurchaseItemSerializerTest(TestCase):
    """ Test case for the PurchaseItem model serializer """

    def setUp(self):
        self.origin_path = os.path.join(
            BASE_DIR, 'website/fixtures/', 'sample_image.jpg'
        )
        self.destination_path = os.path.join(
            BASE_DIR, 'media/', 'sample_image.jpg'
        )

        copyfile(self.origin_path, self.destination_path)

        self.image = open(self.origin_path, 'rb')

        self.category = Category.objects.create(description='Furnitures')

        self.product = Product.objects.create(
            barcode='789789789',
            title='Mattress',
            description='Sleep Mattress',
            image=self.destination_path,
            price=123.000,
            category=self.category
        )

        self.user = User.objects.get_or_create(username='testuser')[0]
        self.purchase_order = PurchaseOrder.objects.create(
            timestamp='2018-10-09T01:15:00Z', user=self.user, cart=False
        )

        self.purchase_item = PurchaseItem(
            id=1,
            title=self.product.title,
            description=self.product.description,
            image=self.destination_path,
            price=self.product.price,
            barcode=self.product.barcode,
            quantity=1.000,
            total_price=self.product.price,
            category=self.product.category,
            purchase_order=self.purchase_order
        )

        self.json = {
            'id': 1,
            'title': self.product.title,
            'description': self.product.description,
            'image': self.product.image,
            'price': self.product.price,
            'barcode': self.product.barcode,
            'quantity': '1.000',
            'total_price': self.product.price,
            'category': self.product.category.id,
            'purchase_order': 1
        }

        self.serializer = PurchaseItemSerializer(
            instance=self.purchase_item
        )

    def test_barcode_content(self):
        """ Test barcode field value """

        self.assertEqual(
            self.purchase_item.barcode,
            self.serializer.data['barcode']
        )

    def test_title_content(self):
        """ Test title field value """

        self.assertEqual(
            self.purchase_item.title,
            self.serializer.data['title']
        )

    def test_description_content(self):
        """ Test description field value """

        self.assertEqual(
            self.purchase_item.description,
            self.serializer.data['description']
        )

    def test_price_content(self):
        """ Test price field value """

        self.assertEqual(
            self.purchase_item.price,
            float(self.serializer.data['price'])
        )

    def test_category_content(self):
        """ Test category id field value """

        self.assertEqual(
            self.purchase_item.category.id,
            self.serializer.data['category']
        )

    def test_blank_barcode(self):
        """ Test using blank barcode value """

        data = self.json
        data.update({'barcode': ''})
        exception_serializer = PurchaseItemSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('barcode', exception_serializer.errors.keys())
        self.assertIn('blank', str(exception_serializer.errors.values()))

    def test_blank_title(self):
        """ Test using blank title value """

        data = self.json
        data.update({'title': ''})
        exception_serializer = PurchaseItemSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('title', exception_serializer.errors.keys())
        self.assertIn('blank', str(exception_serializer.errors.values()))

    def test_blank_description(self):
        """ Test using blank description value """

        data = self.json
        data.update({'description': ''})
        exception_serializer = PurchaseItemSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('description', exception_serializer.errors.keys())
        self.assertIn('blank', str(exception_serializer.errors.values()))

    def test_blank_image(self):
        """ Test using blank image value """

        data = self.json
        data.update({'image': ''})
        exception_serializer = PurchaseItemSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('image', exception_serializer.errors.keys())
        self.assertIn(
            'The submitted data was not a file',
            str(exception_serializer.errors.values())
        )

    def test_blank_price(self):
        """ Test using blank price value """

        data = self.json
        data.update({'price': ''})
        exception_serializer = PurchaseItemSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('price', exception_serializer.errors.keys())
        self.assertIn(
            'valid number', str(exception_serializer.errors.values())
        )

    def test_null_category(self):
        """ Test using null category id value """

        data = self.json
        data.update({'category': ''})
        exception_serializer = ProductSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            exception_serializer.is_valid(raise_exception=True)
        self.assertIn('category', exception_serializer.errors.keys())
        self.assertIn('null', str(exception_serializer.errors.values()))
