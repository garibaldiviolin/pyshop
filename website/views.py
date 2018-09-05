from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView

from .forms import SignUpForm
from .models import Category, Product


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


class LoginView(View):

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


class LogoutView(View):

    def post(self, request, *args, **kwargs):

        logout(request)
        previous_url = request.META.get('HTTP_REFERER')

        return HttpResponseRedirect(previous_url)


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/index'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
