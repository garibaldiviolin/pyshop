""" website views module """

# pylint: disable=W0613, W0221


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.translation import ugettext

from .forms import SignUpForm
from .models import Category, Product, PurchaseOrder, PurchaseItem


class ProductsView(ListView):
    """ ListView that shows all of (or query) the products """

    template_name = 'products.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        """ Returns the queryset of products and categories """

        queryset = Product.objects.all()

        category = self.request.GET.get('category', None)

        if category:
            queryset = queryset.filter(
                category__description=category
            )

        q = self.request.GET.get('q', None)

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            )

        return queryset

    def get_context_data(self, **kwargs):
        """ Mounts the context objects and verifies if user is authenticated
        """

        context = super(ProductsView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['authenticated_user'] = self.request.user
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    """ DetailView for a specific (selected) product """

    template_name = 'product_detail.html'

    def get_object(self, *args, **kwargs):
        """ Returns the product instance by the slug field """

        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug)
        return instance

    def get_context_data(self, **kwargs):
        """ Mounts the context objects and verifies if user is authenticated
        """

        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['authenticated_user'] = self.request.user
        return context


class ProfileView(TemplateView):
    """ View for the users' profiles """

    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        """ Check if user is authenticated, otherwise redirect to sigin page
        """

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('website:signin'))
        return render(
            request, self.template_name, self.get_context_data(**kwargs)
        )

    def get_context_data(self, **kwargs):
        """ Mounts the context objects (including user) """

        context = super(ProfileView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PurchaseOrdersView(TemplateView):
    """ TemplateView for the user's purchase orders """

    template_name = 'purchase_orders.html'

    def get(self, request, *args, **kwargs):
        """ Verify if user is authenticated, otherwise redirect to sigin page
        """

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('website:signin'))
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        """ Makes the purchase_orders list """

        context = super(PurchaseOrdersView, self).get_context_data(**kwargs)
        context['purchase_orders'] = PurchaseOrder.objects.all() \
            .order_by('id').order_by('-cart')
        return context


class PurchaseOrderDetailView(TemplateView):
    """ Shows the purchase order details """

    template_name = 'purchase_order_detail.html'

    def get_context_data(self, **kwargs):
        """ Makes the purchase_order object and the purchase_items list """

        context = super(PurchaseOrderDetailView, self).get_context_data(
            **kwargs
        )
        id = self.kwargs.get('id')
        purchase_order = get_object_or_404(PurchaseOrder, id=id)
        context['purchase_order'] = purchase_order
        purchase_items = PurchaseItem.objects.filter(
            purchase_order_id=purchase_order.id
        )
        if purchase_items.exists():
            context['purchase_items'] = purchase_items
        return context


class CompletePurchaseOrderView(DetailView):
    """ DetailView that changes the purchase order's status (to complete) """

    def get(self, request, *args, **kwargs):
        """ Receives the purchase order's id and changes the cart field to
        False, meaning that the purchase order is completed. After changing
        the status, redirect to the index page
        """
        id = self.kwargs.get('id')

        purchase_order = get_object_or_404(PurchaseOrder, id=id)
        purchase_order.cart = False
        purchase_order.save()

        return HttpResponseRedirect(reverse_lazy('website:index'))


class SignInView(TemplateView):
    """ TemplateView for the user's login """

    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):  # pylint: disable=R0201
        """ Receives the username and password, tries to do the login, and
        then redirect to the index page
        """

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:  # pragma: no cover
                messages.error(request, ugettext('UserIsInactive'))
        else:
            messages.error(request, ugettext('Invalidlogin'))
        return HttpResponseRedirect(reverse_lazy('website:index'))


class SignOutView(View):
    """ View for the user's logout """

    def get(self, request, *args, **kwargs):  # pylint: disable=R0201
        """ Sign the user out and then redirect to the previously accessed
        page
        """

        logout(request)
        previous_url = request.META.get('HTTP_REFERER')

        return HttpResponseRedirect(previous_url)


class SignUpView(CreateView):
    """ CreateView for the users' registration """

    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('website:index')

    def form_valid(self, form):
        """ Check if form is valid and then save it """

        form.save()
        return super().form_valid(form)


class AddToCartView(View):
    """ View to add item to user's cart """

    def post(self, request, *args, **kwargs):
        """ Check if user is authenticated, otherwise redirect to the sigin
        Then it expects the product_id that the user wants to add to the cart.
        If the user doesn't have any pending purchase order (cart=True), a new
        order is created, with the new item, and the user is redirected to the
        previously accessed page.
        """

        previous_url = request.META.get('HTTP_REFERER')

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('website:signin'))

        product_id = request.POST.get('product_id', None)
        product = get_object_or_404(Product, barcode=product_id)

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
