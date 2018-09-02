import pdb

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.db.models import Q

from .models import Product


class ProductsView(ListView):

    template_name = "products.html"
    context_object_name = 'product_list'

    def get_queryset(self):
        queryset = Product.objects.all()

        q = self.request.GET.get('q', '')

        if len(q) > 0:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['authenticated_user'] = self.request.user
        return context


class LoginView(View):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        pdb.set_trace()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Hello, ' + username + '!')
            else:
                return HttpResponse('Your account has been disabled')
        else:
            return HttpResponse('Invalid login')
