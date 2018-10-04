from rest_framework import serializers

from website.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for the Category model """

    class Meta:
        model = Category
        exclude = ('id', )


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer for the Product model """

    class Meta:
        model = Product
        exclude = ('slug', )
