from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Order(models.Model):
    status_pending = 'Pending'
    status_processing = 'Processing'
    status_completed = 'Completed'

    STATUS_CHOICES = {
        (status_pending, 'Pending'),
        (status_processing, 'Processing'),
        (status_completed, 'Completed'),
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Содержание заказа')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=status_pending, verbose_name='Статус заказа')

    def __str__(self):
        return f'{self.content}, {self.status}'
