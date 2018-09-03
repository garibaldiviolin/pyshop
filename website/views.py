from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
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

        previous_url = request.META.get('HTTP_REFERER')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(previous_url)
            else:
                return HttpResponse('User is inactive')
        else:
            return HttpResponse('Invalid login')


class LogoutView(View):

    def post(self, request, *args, **kwargs):

        logout(request)
        previous_url = request.META.get('HTTP_REFERER')

        return HttpResponseRedirect(previous_url)
