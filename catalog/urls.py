from django.urls import path
from . import views
from .views import ProductListView, ContactsView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('home/', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]