from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('order/create/', OrderCreate.as_view(), name='order_create'),
    path('profile/', Profile.as_view(), name='profile'),
]