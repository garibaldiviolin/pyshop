from django.contrib.auth.models import User
from django.test import TestCase

from website.forms import SignUpForm


class SignUpFormTest(TestCase):
    """ Test case for SignUpForm """

    def setUp(self):
        self.user = User.objects.create(
            username='user12',
            first_name='firstname',
            last_name='lastname',
            email='user12@company.com',
            password='okabc321'
        )

        self.form = SignUpForm(
            data={
                'username': 'user123',
                'first_name': 'firstname',
                'last_name': 'lastname',
                'email': 'user123@company.com',
                'password1': 'okabc321',
                'password2': 'okabc321'
            }
        )

    def test_valid_form(self):
        self.assertTrue(self.form.is_valid())

    def test_remove_username(self):
        invalid_form = self.form
        del invalid_form.data['email']
        self.assertFalse(invalid_form.is_valid())

    def test_invalid_email(self):
        invalid_form = self.form
        invalid_form.data['email'] = 'ok'
        self.assertFalse(invalid_form.is_valid())

    def test_invalid_password1(self):
        invalid_form = self.form
        invalid_form.data['password1'] = 'ok'
        self.assertFalse(invalid_form.is_valid())

    def test_invalid_password2(self):
        invalid_form = self.form
        invalid_form.data['password2'] = 'ok'
        self.assertFalse(invalid_form.is_valid())
