from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}! Данные успешно отправлены.')
    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context=context)

