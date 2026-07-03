from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        self.send_welcome_email(user.email)
        return response

    def send_welcome_email(self, user_email):
        subjects = 'Добро пожаловать в наш сервис'
        message = 'Спасибо что зарегистрировались в нашем сервисе'
        from_email = 'r4buzyarov@yandex.ru'
        recipient_list = [user_email]
        send_mail(subjects, message, from_email, recipient_list)