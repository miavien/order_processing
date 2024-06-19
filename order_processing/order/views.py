from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import *

class OrderCreate(CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'order_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')

class Profile(TemplateView):
    template_name = 'profile.html'

    # def get_context_data(self, **kwargs):
