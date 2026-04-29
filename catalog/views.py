from django.shortcuts import render
from django.http import HttpResponse
from models import Product

# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}! Данные успешно отправлены.')
    return render(request, 'catalog/contacts.html')

def product_details(request, pk):
    products = Product.objects.all(pk=pk)
    context = {
        'products': products
    }
    return render(request, 'product_details', context=context)