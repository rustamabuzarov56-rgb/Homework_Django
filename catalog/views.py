from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DeleteView
from django.views import  View

from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

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

class ProductDetailView(DeleteView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
