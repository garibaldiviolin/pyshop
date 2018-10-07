from django.test import TestCase
from django.urls import reverse

from website.models import Category, Product


class IndexViewTest(TestCase):
    """ Test case for the IndexView """

    def test_index(self):
        """ Test index get request """
        response = self.client.get(reverse('manager:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class CategoriesManagementViewTest(TestCase):
    """ Test case for the CategoriesManagementView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()

    def test_categories(self):
        """ Test categories GET request """
        response = self.client.get(reverse('manager:categories'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context_data['categories']),
            list(self.category_queryset)
        )
        self.assertTemplateUsed(response, 'categories_management.html')


class CategoryEditViewTest(TestCase):
    """ Test case for the CategoryEditView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()

    def test_valid_category_edit(self):
        """ Test valid category edit GET request """
        response = self.client.get(reverse('manager:category-edit', args=(1,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_edit.html')

    def test_invalid_category_edit(self):
        """ Test invalid category edit GET request """
        response = self.client.get(reverse('manager:category-edit', args=(2,)))

        self.assertEqual(response.status_code, 404)

    def test_invalid_form(self):
        """ Test invalid category form POST request """
        response = self.client.post(
            reverse('manager:category-edit', args=(1,)),
            {'invalid_field': 'invalid_content'}
        )
        self.assertFalse(response.context['form'].is_valid())

    def test_valid_form(self):
        """ Test valid category form POST request """
        response = self.client.post(
            reverse('manager:category-edit', args=(1,)),
            {'description': 'furniture'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url, reverse('manager:categories'))


class CategoryDeleteViewTest(TestCase):
    """ Test case for the CategoryDeleteView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )

        self.category_queryset = Category.objects.all()

    def test_valid_category_edit(self):
        """ Test valid category delete GET request """
        response = self.client.get(
            reverse('manager:category-delete', args=(1,))
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html')

    def test_invalid_category_edit(self):
        """ Test invalid category delete GET request """
        response = self.client.get(
            reverse('manager:category-delete', args=(2,))
        )

        self.assertEqual(response.status_code, 404)


class ProductsManagementViewTest(TestCase):
    """ Test case for the ProductsManagementView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        Product.objects.create(
            barcode='5901234123457', title='Mattress',
            description='Mattress', image='mattress.jpg', price=800.724,
            category=self.category
        )

        self.category_queryset = Category.objects.all()
        self.product_queryset = Product.objects.all()

    def test_categories(self):
        """ Test valid product GET request """
        response = self.client.get(reverse('manager:products'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context_data['products']),
            list(self.product_queryset)
        )
        self.assertTemplateUsed(response, 'products_management.html')


class ProductEditViewTest(TestCase):
    """ Test case for the ProductEditView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product.objects.create(
            barcode='5901234123457', title='Mattress',
            description='Mattress', image='mattress.jpg', price=800.724,
            category=self.category
        )

    def test_valid_product_edit(self):
        """ Test valid product edit GET request """
        response = self.client.get(
            reverse('manager:product-edit', args=(self.product.slug,))
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_edit.html')

    def test_invalid_product_edit(self):
        """ Test invalid product edit GET request """
        response = self.client.get(reverse('manager:product-edit', args=(2,)))

        self.assertEqual(response.status_code, 404)

    def test_invalid_form(self):
        """ Test valid product form POST request """
        response = self.client.post(
            reverse('manager:product-edit', args=(self.product.slug,)),
            {'invalid_field': 'invalid_content'}
        )
        self.assertFalse(response.context['form'].is_valid())

    def test_valid_form(self):
        """ Test valid product form POST request """
        response = self.client.post(
            reverse('manager:product-edit', args=(self.product.slug,)),
            {
                'barcode': '5901234123457',
                'title': 'Mattress',
                'description': 'Mattress',
                'image': 'mattress.jpg',
                'price': 800.724,
                'category': 1
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url, reverse('manager:products'))


class ProductDeleteViewTest(TestCase):
    """ Test case for the ProductDeleteView """

    def setUp(self):
        self.category = Category.objects.create(
            description='Category'
        )
        self.product = Product.objects.create(
            barcode='5901234123457', title='Mattress',
            description='Mattress', image='mattress.jpg', price=800.724,
            category=self.category
        )

    def test_valid_category_edit(self):
        """ Test valid product edit POST request """
        response = self.client.get(
            reverse('manager:product-delete', args=(self.product.slug,))
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html')

    def test_invalid_category_edit(self):
        """ Test invalid product edit POST request """
        response = self.client.get(
            reverse('manager:product-delete', args=(2,))
        )

        self.assertEqual(response.status_code, 404)
