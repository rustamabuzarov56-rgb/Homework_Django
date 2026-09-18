from gc import get_objects
from itertools import product

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DeleteView, DetailView
from django.views import  View

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden

from .services import ProductService
from catalog.forms import ProductForm
from catalog.models import Product
from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductUnpublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет разрешения на снятие продукта с публикации')
        product.is_published = False
        product.save()
        return redirect('catalog:product_detail', pk=pk)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}, данные успешно отправлены')

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg) or self.kwargs.get('pk')
        cache_key = f"product_{pk}"
        cached_product = cache.get(cache_key)

        if not cached_product:
            cached_product = super().get_object(queryset)
            cache.set(cache_key, cached_product, 60 * 15)
        return cached_product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)

        if product.owner != self.request.user:
            raise PermissionDenied
        return product

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)

        is_owner = product.owner == self.request.user
        is_moderator = self.request.user.has_perm('catalog.delete_product')

        if not(is_owner or is_moderator):
            raise PermissionDenied
        return product

class CategoryProductListView(ListView):
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return ProductService.product_get_by_category(pk)