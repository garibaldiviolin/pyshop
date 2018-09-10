import pdb

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import SignUpForm
from .models import Category, Product, PurchaseOrder, PurchaseItem


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


class ProfileView(TemplateView):

    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('website:signin'))
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(
            *args, **kwargs
        )
        context['user'] = self.request.user
        return context


class UserPurchaseView(TemplateView):

    template_name = 'user_purchases.html'

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('website:signin'))
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, *args, **kwargs):
        context = super(UserPurchaseView, self).get_context_data(
            *args, **kwargs
        )
        context['purchase_orders'] = PurchaseOrder.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                messages.error(request, 'User is inactive')
        else:
            messages.error(request, 'Invalid login')
        return HttpResponseRedirect(reverse_lazy('website:index'))


class SignInView(TemplateView):

    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                messages.error(request, 'User is inactive')
        else:
            messages.error(request, 'Invalid login')
        return HttpResponseRedirect(reverse_lazy('website:index'))


class SignOutView(View):

    def get(self, request, *args, **kwargs):

        logout(request)
        previous_url = request.META.get('HTTP_REFERER')

        return HttpResponseRedirect(previous_url)


class SignUpView(CreateView):

    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('website:index')

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


class AddToCartView(View):

    def post(self, request, *args, **kwargs):

        previous_url = request.META.get('HTTP_REFERER')

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('website:signin'))

        product_id = request.POST.get('product_id', None)
        product_queryset = Product.objects.filter(barcode=product_id)

        if not product_queryset.exists():
            messages.error(request, 'Product does not exists')
            return HttpResponseRedirect(previous_url)
        product = product_queryset.first()

        pdb.set_trace()

        user = self.request.user

        order_queryset = PurchaseOrder.objects.filter(
            Q(user=user) & Q(cart=True)
        )
        if order_queryset.exists():
            purchase_order = order_queryset.first()
        else:
            purchase_order = PurchaseOrder.objects.create(
                timestamp=timezone.now(), user=user, cart=True
            )

        PurchaseItem.objects.create(
            barcode=product.barcode, title=product.title,
            description=product.description, image=product.image,
            price=product.price, category=product.category,
            purchase_order=purchase_order, quantity=1.000,
            total_price=product.price
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
