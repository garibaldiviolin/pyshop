from django.test import TestCase
from django.utils.translation import ugettext_lazy
from django.utils.translation import activate


class BrazilianPortugueseTest(TestCase):
    """ Test case for the 'pt-br' internationalization (i18n) strings """

    def setUp(self):
        activate('pt-br')
        self.client.LANGUAGE_CODE = 'pt-br'

    def test_translated_strings(self):
        """ Test translation of strings to 'pt-br' language """

        self.assertEqual('Desconectar', ugettext_lazy('SignOut'))
        self.assertEqual('Página Inicial', ugettext_lazy('HomePage'))
        self.assertEqual('Título', ugettext_lazy('Title'))
        self.assertEqual('Descrição', ugettext_lazy('Description'))
        self.assertEqual('Preço', ugettext_lazy('Price'))
        self.assertEqual('Lista de Produtos', ugettext_lazy('ProductsList'))
        self.assertEqual('Detalhes', ugettext_lazy('Details'))
        self.assertEqual('Meu Perfil', ugettext_lazy('MyProfile'))
        self.assertEqual('Usuário', ugettext_lazy('Username'))
        self.assertEqual('Senha', ugettext_lazy('Password'))
        self.assertEqual('Conectar', ugettext_lazy('SignIn'))
        self.assertEqual('Registrar-se', ugettext_lazy('SignUp'))
        self.assertEqual('Adicionar ao Carrinho', ugettext_lazy('AddToCart'))
        self.assertEqual('Minhas Compras', ugettext_lazy('MyPurchases'))
        self.assertEqual('Primeiro Nome', ugettext_lazy('FirstName'))
        self.assertEqual('Sobrenome', ugettext_lazy('LastName'))
        self.assertEqual('Pendente', ugettext_lazy('Pending'))
        self.assertEqual('Completada', ugettext_lazy('Completed'))
        self.assertEqual('Gerência', ugettext_lazy('Manager'))
        self.assertEqual('Produto', ugettext_lazy('Product'))
        self.assertEqual('Produtos', ugettext_lazy('Products'))
        self.assertEqual('Novo Produto', ugettext_lazy('NewProduct'))
        self.assertEqual('Código de Barras', ugettext_lazy('Barcode'))
        self.assertEqual('Editar', ugettext_lazy('Edit'))
        self.assertEqual('Excluir', ugettext_lazy('Delete'))
        self.assertEqual(
            'Tem certeza que deseja excluir',
            ugettext_lazy('AreYouSureYouWantToDelete')
        )
        self.assertEqual('Confirmar', ugettext_lazy('Confirm'))
        self.assertEqual('Salvar', ugettext_lazy('Save'))
        self.assertEqual('Categoria', ugettext_lazy('Category'))
        self.assertEqual('Categorias', ugettext_lazy('Categories'))
        self.assertEqual('Nova Categoria', ugettext_lazy('NewCategory'))
        self.assertEqual(
            'Usuário e/ou senha inválido(s).',
            ugettext_lazy('Invalidlogin')
        )
        self.assertEqual(
            'O usuário está inativo.',
            ugettext_lazy('UserIsInactive')
        )
        self.assertEqual(
            'O produto não existe.',
            ugettext_lazy('ProductDoesNotExist')
        )
        self.assertEqual('Módulo Gerência', ugettext_lazy('ManagerModule'))


class EnglishTest(TestCase):
    """ Test case for the 'en' internationalization (i18n) strings """

    def setUp(self):
        activate('en')
        self.client.LANGUAGE_CODE = 'en'

    def test_translated_strings(self):
        """ Test translation of strings to 'en' language """

        self.assertEqual('Sign Out', ugettext_lazy('SignOut'))
        self.assertEqual('Home Page', ugettext_lazy('HomePage'))
        self.assertEqual('Title', ugettext_lazy('Title'))
        self.assertEqual('Description', ugettext_lazy('Description'))
        self.assertEqual('Price', ugettext_lazy('Price'))
        self.assertEqual('Products List', ugettext_lazy('ProductsList'))
        self.assertEqual('Details', ugettext_lazy('Details'))
        self.assertEqual('My Profile', ugettext_lazy('MyProfile'))
        self.assertEqual('Username', ugettext_lazy('Username'))
        self.assertEqual('Password', ugettext_lazy('Password'))
        self.assertEqual('Sign In', ugettext_lazy('SignIn'))
        self.assertEqual('Sign Up', ugettext_lazy('SignUp'))
        self.assertEqual('Add To Cart', ugettext_lazy('AddToCart'))
        self.assertEqual('My Purchases', ugettext_lazy('MyPurchases'))
        self.assertEqual('First Name', ugettext_lazy('FirstName'))
        self.assertEqual('Last Name', ugettext_lazy('LastName'))
        self.assertEqual('Pending', ugettext_lazy('Pending'))
        self.assertEqual('Completed', ugettext_lazy('Completed'))
        self.assertEqual('Manager', ugettext_lazy('Manager'))
        self.assertEqual('Product', ugettext_lazy('Product'))
        self.assertEqual('Products', ugettext_lazy('Products'))
        self.assertEqual('New Product', ugettext_lazy('NewProduct'))
        self.assertEqual('Barcode', ugettext_lazy('Barcode'))
        self.assertEqual('Edit', ugettext_lazy('Edit'))
        self.assertEqual('Delete', ugettext_lazy('Delete'))
        self.assertEqual(
            'Are you sure you want to delete',
            ugettext_lazy('AreYouSureYouWantToDelete')
        )
        self.assertEqual('Confirm', ugettext_lazy('Confirm'))
        self.assertEqual('Save', ugettext_lazy('Save'))
        self.assertEqual('Category', ugettext_lazy('Category'))
        self.assertEqual('Categories', ugettext_lazy('Categories'))
        self.assertEqual('New Category', ugettext_lazy('NewCategory'))
        self.assertEqual('Invalid login.', ugettext_lazy('Invalidlogin'))
        self.assertEqual('User is inactive.', ugettext_lazy('UserIsInactive'))
        self.assertEqual(
            'Product does not exist.',
            ugettext_lazy('ProductDoesNotExist')
        )
        self.assertEqual('Manager Module', ugettext_lazy('ManagerModule'))
