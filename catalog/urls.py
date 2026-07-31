from django.urls import path

from . import views
from .views import (ProductListView, ContactsView, ProductDetailView, ProductUpdateView, ProductCreateView,
                    ProductDeleteView, ProductUnpublishView)

app_name = 'catalog'

urlpatterns = [
    path('home/', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_form/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_form/', ProductCreateView.as_view(), name='product_create'),
    path('product_confirm_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/unpublish/<int:pk>/', ProductUnpublishView.as_view(), name='product_unpublish'),
]