from rest_framework import serializers

from website.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for the Category model """

    class Meta:
        model = Category
        exclude = ('id', )
