""" restapi serializers (Django REST Framework) """

from rest_framework import serializers

from website.models import Category, Product, PaymentMethod


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for the Category model """

    class Meta:
        """ CategorySerializer's Meta class """

        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer for the Product model """

    class Meta:
        """ ProductSerializer's Meta class """

        model = Product
        exclude = ('slug', )


class PaymentMethodSerializer(serializers.ModelSerializer):
    """ Serializer for the PaymentMethod model """

    class Meta:
        """ PaymentMethodSerializer's Meta class """

        model = PaymentMethod
        fields = '__all__'
