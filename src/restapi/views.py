from rest_framework.generics import CreateAPIView

from website.models import Category
from .serializers import CategorySerializer


class CategoryCreateView(CreateAPIView):
    """ Create view for Category objects """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'description'
