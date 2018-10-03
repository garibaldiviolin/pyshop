from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from website.models import Category, Product, PurchaseOrder


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


class ProductDetailViewTest(TestCase):
    """ Test case for the ProductDetailView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product(
            barcode='2012345012349', slug=None, title='Wardrobe',
            description='Lorem ipsum', image='wardrobe.jpeg', price=55.990,
            category=self.category
        )

    def test_product_detail(self):
        response = self.client.get(
            reverse('website:product-detail', args=(self.product.slug,))
        )

        self.assertEqual(response.status_code, 404)


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


class PurchaseOrdersViewTest(TestCase):
    """ Test case for the PurchaseOrdersView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()
        self.client.force_login(
            User.objects.get_or_create(username='testuser')[0]
        )

    def test_product_detail(self):
        response = self.client.get(reverse('website:purchase-orders'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purchase_orders.html')


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

    def test_product_detail(self):
        response = self.client.get(
            reverse('website:purchase-order', args=(1,))
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'purchase_order_detail.html')


class CompletePurchaseOrderViewTest(TestCase):
    """ Test case for the CompletePurchaseOrderView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()

    def test_product_detail(self):
        response = self.client.get(
            reverse('website:complete-purchase-order', args=(1,))
        )

        self.assertEqual(response.status_code, 404)


class SignInViewTest(TestCase):
    """ Test case for the SignInView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()

    def test_product_detail(self):
        response = self.client.get(reverse('website:signin'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')


class SignOutViewTest(TestCase):
    """ Test case for the SignOutView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()

    def test_product_detail(self):
        response = self.client.get(reverse('website:signout'))

        self.assertEqual(response.status_code, 302)


class SignUpViewTest(TestCase):
    """ Test case for the SignUpView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()

    def test_product_detail(self):
        response = self.client.get(reverse('website:signup'))

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

    def test_product_detail(self):
        response = self.client.get(reverse('website:add-to-cart'))

        self.assertEqual(response.status_code, 405)
