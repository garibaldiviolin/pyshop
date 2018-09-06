from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404

from .forms import SignUpForm
from .models import Category, Product, CartProduct


class ProductsView(ListView):

    template_name = "products.html"
    context_object_name = 'product_list'

    def get_queryset(self):

        queryset = Product.objects.all()

        category = self.request.GET.get('category', '')

        if len(category) > 0:
            queryset = queryset.filter(
                category__description=category
            )

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

        context['categories'] = Category.objects.all()
        return context


class SignInView(View):

    def post(self, request, *args, **kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')

        previous_url = request.META.get('HTTP_REFERER')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                messages.error(request, 'User is inactive')
        else:
            messages.error(request, 'Invalid login')
        return HttpResponseRedirect(previous_url)


class SignOutView(View):

    def post(self, request, *args, **kwargs):

        logout(request)
        previous_url = request.META.get('HTTP_REFERER')

        return HttpResponseRedirect(previous_url)


class SignUpView(CreateView):

    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = 'website:index'

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


class AddToCartView(View):

    def post(self, request, *args, **kwargs):

        previous_url = request.META.get('HTTP_REFERER')

        product_id = request.POST.get('product_id', None)
        product_queryset = Product.objects.filter(barcode=product_id)

        if not product_queryset.exists():
            messages.error(request, 'User is inactive')
            return HttpResponseRedirect(previous_url)
        product = product_queryset.first()

        if not request.session.exists(request.session.session_key):
            request.session.create()

        if request.user.is_authenticated:
            anonymous_user = None
            user = self.request.user
        else:
            anonymous_user = request.session['anonymous_user'] \
                = request.session.session_key
            user = None

        CartProduct.objects.create(
            user=user, anonymous_user=anonymous_user, product=product,
            quantity=1.000, total_price=product.price
        )

        return HttpResponseRedirect(previous_url)


class ProductDetailView(DetailView):

    template_name = 'product_detail.html'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug)
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs
        )
        return context
