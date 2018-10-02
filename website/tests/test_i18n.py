from django.test import TestCase
from django.utils.translation import ugettext_lazy
from django.utils.translation import activate


class BrazilianPortugueseTest(TestCase):
    """ Test case for the 'pt-br' internationalization (i18n) strings """

    def setUp(self):
        activate('pt-br')
        self.client.LANGUAGE_CODE = 'pt-br'

    def test_translated_strings(self):
        self.assertEquals('Desconectar', ugettext_lazy('SignOut'))
        self.assertEquals('Página Inicial', ugettext_lazy('HomePage'))
        self.assertEquals('Título', ugettext_lazy('Title'))
        self.assertEquals('Descrição', ugettext_lazy('Description'))
        self.assertEquals('Preço', ugettext_lazy('Price'))
        self.assertEquals('Lista de Produtos', ugettext_lazy('ProductsList'))
        self.assertEquals('Detalhes', ugettext_lazy('Details'))
        self.assertEquals('Meu Perfil', ugettext_lazy('MyProfile'))
        self.assertEquals('Usuário', ugettext_lazy('Username'))
        self.assertEquals('Senha', ugettext_lazy('Password'))
        self.assertEquals('Conectar', ugettext_lazy('SignIn'))
        self.assertEquals('Registrar-se', ugettext_lazy('SignUp'))
        self.assertEquals('Adicionar ao Carrinho', ugettext_lazy('AddToCart'))
        self.assertEquals('Minhas Compras', ugettext_lazy('MyPurchases'))
        self.assertEquals('Primeiro Nome', ugettext_lazy('FirstName'))
        self.assertEquals('Sobrenome', ugettext_lazy('LastName'))
        self.assertEquals('Pendente', ugettext_lazy('Pending'))
        self.assertEquals('Completada', ugettext_lazy('Completed'))
        self.assertEquals('Gerência', ugettext_lazy('Manager'))
        self.assertEquals('Produto', ugettext_lazy('Product'))
        self.assertEquals('Produtos', ugettext_lazy('Products'))
        self.assertEquals('Novo Produto', ugettext_lazy('NewProduct'))
        self.assertEquals('Código de Barras', ugettext_lazy('Barcode'))
        self.assertEquals('Editar', ugettext_lazy('Edit'))
        self.assertEquals('Excluir', ugettext_lazy('Delete'))
        self.assertEquals(
            'Tem certeza que deseja excluir',
            ugettext_lazy('AreYouSureYouWantToDelete')
        )
        self.assertEquals('Confirmar', ugettext_lazy('Confirm'))
        self.assertEquals('Salvar', ugettext_lazy('Save'))
        self.assertEquals('Categoria', ugettext_lazy('Category'))
        self.assertEquals('Categorias', ugettext_lazy('Categories'))
        self.assertEquals('Nova Categoria', ugettext_lazy('NewCategory'))
        self.assertEquals(
            'Usuário e/ou senha inválido(s).',
            ugettext_lazy('Invalidlogin')
        )
        self.assertEquals(
            'O usuário está inativo.',
            ugettext_lazy('UserIsInactive')
        )
        self.assertEquals(
            'O produto não existe.',
            ugettext_lazy('ProductDoesNotExist')
        )
        self.assertEquals('Módulo Gerência', ugettext_lazy('ManagerModule'))


class EnglishTest(TestCase):
    """ Test case for the 'en' internationalization (i18n) strings """

    def setUp(self):
        activate('en')
        self.client.LANGUAGE_CODE = 'en'

    def test_translated_strings(self):
        self.assertEquals('Sign Out', ugettext_lazy('SignOut'))
        self.assertEquals('Home Page', ugettext_lazy('HomePage'))
        self.assertEquals('Title', ugettext_lazy('Title'))
        self.assertEquals('Description', ugettext_lazy('Description'))
        self.assertEquals('Price', ugettext_lazy('Price'))
        self.assertEquals('Products List', ugettext_lazy('ProductsList'))
        self.assertEquals('Details', ugettext_lazy('Details'))
        self.assertEquals('My Profile', ugettext_lazy('MyProfile'))
        self.assertEquals('Username', ugettext_lazy('Username'))
        self.assertEquals('Password', ugettext_lazy('Password'))
        self.assertEquals('Sign In', ugettext_lazy('SignIn'))
        self.assertEquals('Sign Up', ugettext_lazy('SignUp'))
        self.assertEquals('Add To Cart', ugettext_lazy('AddToCart'))
        self.assertEquals('My Purchases', ugettext_lazy('MyPurchases'))
        self.assertEquals('First Name', ugettext_lazy('FirstName'))
        self.assertEquals('Last Name', ugettext_lazy('LastName'))
        self.assertEquals('Pending', ugettext_lazy('Pending'))
        self.assertEquals('Completed', ugettext_lazy('Completed'))
        self.assertEquals('Manager', ugettext_lazy('Manager'))
        self.assertEquals('Product', ugettext_lazy('Product'))
        self.assertEquals('Products', ugettext_lazy('Products'))
        self.assertEquals('New Product', ugettext_lazy('NewProduct'))
        self.assertEquals('Barcode', ugettext_lazy('Barcode'))
        self.assertEquals('Edit', ugettext_lazy('Edit'))
        self.assertEquals('Delete', ugettext_lazy('Delete'))
        self.assertEquals(
            'Are you sure you want to delete',
            ugettext_lazy('AreYouSureYouWantToDelete')
        )
        self.assertEquals('Confirm', ugettext_lazy('Confirm'))
        self.assertEquals('Save', ugettext_lazy('Save'))
        self.assertEquals('Category', ugettext_lazy('Category'))
        self.assertEquals('Categories', ugettext_lazy('Categories'))
        self.assertEquals('New Category', ugettext_lazy('NewCategory'))
        self.assertEquals('Invalid login.', ugettext_lazy('Invalidlogin'))
        self.assertEquals('User is inactive.', ugettext_lazy('UserIsInactive'))
        self.assertEquals(
            'Product does not exist.',
            ugettext_lazy('ProductDoesNotExist')
        )
        self.assertEquals('Manager Module', ugettext_lazy('ManagerModule'))
