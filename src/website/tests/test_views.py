""" This module tests website app views """

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from website.models import (
    Category,
    Product,
    PurchaseOrder,
    PurchaseItem
)


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
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.client.force_login(
            self.user
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

    def test_query_products(self):
        response = self.client.get(
            reverse('website:index'),
            {
                'category': 'Category',
                'q': 'Mattress'
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context_data['product_list']),
            list(self.product_queryset)
        )
        self.assertEqual(
            list(response.context_data['categories']),
            list(self.category_queryset)
        )

    def test_not_logged_user(self):
        self.client.logout()
        response = self.client.get(
            reverse('website:index'),
            {
                'category': 'Category',
                'q': 'Mattress'
            }
        )
        self.assertEqual(response.status_code, 200)


class ProductDetailViewTest(TestCase):
    """ Test case for the ProductDetailView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product.objects.create(
            barcode='2012345012349', slug=None, title='Wardrobe',
            description='Lorem ipsum', image='wardrobe.jpeg', price=55.990,
            category=self.category
        )
        self.client.force_login(
            User.objects.get_or_create(username='testuser')[0]
        )

    def test_product_detail(self):
        response = self.client.get(
            reverse('website:product-detail', args=(self.product.slug,))
        )

        self.assertEqual(response.status_code, 200)

    def test_not_logged_user(self):
        self.client.logout()
        response = self.client.get(
            reverse('website:product-detail', args=(self.product.slug,))
        )

        self.assertEqual(response.status_code, 200)


class ProfileViewTest(TestCase):
    """ Test case for the ProfileView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()
        self.client.force_login(
            User.objects.get_or_create(username='testuser')[0]
        )

    def test_product_detail(self):
        response = self.client.get(reverse('website:profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_not_logged_user(self):
        self.client.logout()
        response = self.client.get(reverse('website:profile'))

        self.assertEqual(response.status_code, 302)


class PurchaseOrdersViewTest(TestCase):
    """ Test case for the PurchaseOrdersView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product.objects.create(
            barcode='2012345012349', slug=None, title='Wardrobe',
            description='Lorem ipsum', image='wardrobe.jpeg', price=55.990,
            category=self.category
        )
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.client.force_login(
            self.user
        )
        self.purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(), user=self.user, cart=False
        )

    def test_purchase_orders(self):
        response = self.client.get(reverse('website:purchase-orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purchase_orders.html')

    def test_not_logged_user(self):
        self.client.logout()
        response = self.client.get(reverse('website:purchase-orders'))

        self.assertEqual(response.status_code, 302)


class PurchaseOrderDetailViewTest(TestCase):
    """ Test case for the PurchaseOrderDetailView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product.objects.create(
            barcode='2012345012349', slug=None, title='Wardrobe',
            description='Lorem ipsum', image='wardrobe.jpeg', price=55.990,
            category=self.category
        )
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.client.force_login(
            self.user
        )
        self.purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(), user=self.user, cart=False
        )
        self.purchase_item = PurchaseItem.objects.create(
            barcode=self.product.barcode,
            title=self.product.title,
            description=self.product.description,
            image=self.product.image,
            price=self.product.price,
            category=self.product.category,
            purchase_order=self.purchase_order,
            quantity=1,
            total_price=1
        )

    def test_purchase_order_detail(self):
        response = self.client.get(
            reverse('website:purchase-order', args=(self.purchase_order.id,))
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purchase_order_detail.html')

    def test_invalid_purchase_order_detail(self):
        response = self.client.get(
            reverse('website:purchase-order', args=(2,))
        )

        self.assertEqual(response.status_code, 404)


class CompletePurchaseOrderViewTest(TestCase):
    """ Test case for the CompletePurchaseOrderView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product.objects.create(
            barcode='2012345012349', slug=None, title='Wardrobe',
            description='Lorem ipsum', image='wardrobe.jpeg', price=55.990,
            category=self.category
        )
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.client.force_login(
            self.user
        )
        self.purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(), user=self.user, cart=False
        )

    def test_complete_purchase_order(self):
        response = self.client.get(reverse(
            'website:complete-purchase-order', args=(self.purchase_order.id,)
        ))

        self.assertEqual(response.status_code, 302)

    def test_complete_invalid_purchase_order(self):
        response = self.client.get(reverse(
            'website:complete-purchase-order', args=(2,)
        ))

        self.assertEqual(response.status_code, 404)


class SignInViewTest(TestCase):
    """ Test case for the SignInView """

    def setUp(self):
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.user.is_active = True
        self.user.set_password('okok321')
        self.user.save()

    def test_get_sigin(self):
        response = self.client.get(reverse('website:signin'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    def test_post_sigin(self):
        self.user.save()
        response = self.client.post(
            reverse('website:signin'),
            {
                'username': 'testuser',
                'password': 'okok321'
            }
        )

        self.assertEqual(response.status_code, 302)

    def test_invalid_user(self):
        response = self.client.post(
            reverse('website:signin'),
            {
                'username': 'invalid_user',
                'password': 'okok321'
            }
        )

        self.assertEqual(response.status_code, 302)

    def test_inactive_user(self):
        self.user.is_active = False  # change to inactive to test
        self.user.save()
        response = self.client.post(
            reverse('website:signin'),
            {
                'username': 'testuser',
                'password': 'okok321'
            }
        )

        self.assertEqual(response.status_code, 302)


class SignOutViewTest(TestCase):
    """ Test case for the SignOutView """

    def setUp(self):
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.client.force_login(
            self.user
        )

    def teste_signout(self):
        response = self.client.get(reverse('website:signout'))
        self.assertEqual(response.status_code, 302)


class SignUpViewTest(TestCase):
    """ Test case for the SignUpView """

    def test_get(self):
        response = self.client.get(reverse('website:signup'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_post_valid_user(self):
        response = self.client.post(
            reverse('website:signup'),
            {
                'username': 'test_user',
                'first_name': 'first',
                'last_name': 'last',
                'email': 'test_user@admin.com',
                'password1': 'okok321321',
                'password2': 'okok321321'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_post_invalid_user(self):
        response = self.client.post(
            reverse('website:signup'),
            {
                'username': 'test_user',
                'first_name': 'first',
                'last_name': 'last',
                'email': 'test_user@admin.com',
                'password1': 'okok321321',
                'password2': 'test'  # both passwords must be the same
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')


class AddToCartViewTest(TestCase):
    """ Test case for the AddToCartView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product.objects.create(
            barcode='2012345012349', slug=None, title='Wardrobe',
            description='Lorem ipsum', image='wardrobe.jpeg', price=55.990,
            category=self.category
        )
        self.user = User.objects.get_or_create(username='testuser')[0]
        self.client.force_login(
            self.user
        )
        self.purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(), user=self.user, cart=False
        )

    def test_add_valid_product(self):
        response = self.client.post(
            reverse('website:add-to-cart'),
            {
                'product_id': '2012345012349'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_add_invalid_product(self):
        response = self.client.post(
            reverse('website:add-to-cart'),
            {
                'product_id': '9999999999999'
            }
        )
        self.assertEqual(response.status_code, 404)

    def test_new_purchase_order(self):
        self.purchase_order.cart = True
        self.purchase_order.save()
        response = self.client.post(
            reverse('website:add-to-cart'),
            {
                'product_id': '2012345012349'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_not_logged_user(self):
        self.client.logout()
        response = self.client.post(
            reverse('website:add-to-cart'),
            {
                'product_id': '2012345012349'
            }
        )
        self.assertEqual(response.status_code, 302)
