from django.urls import path

from .views import CategoryCreateView


urlpatterns = [
    path(
        'v1/categories/',
        CategoryCreateView.as_view(),
        name='categories'
    ),
]
