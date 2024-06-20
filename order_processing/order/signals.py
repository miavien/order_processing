from django.db.models.signals import post_save, pre_save
from .models import *
from .tasks import *
from django.dispatch import receiver

@receiver(post_save, sender=Order)
def status_changed_handler(sender, instance, created, **kwargs):
    if not created:
        if instance.status != 'Pending':
            new_status = instance.status
            status_changed_email.delay(instance.id, new_status)

@receiver(post_save, sender=Order)
def order_created_handler(sender, instance, created, **kwargs):
    if created:
        order_created_email.delay(instance.id)