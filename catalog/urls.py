from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
]