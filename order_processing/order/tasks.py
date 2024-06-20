from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from order_processing import settings
from .models import *

@shared_task
def status_changed_email(order_id, new_status):
    order = Order.objects.get(pk=order_id)
    user_email = order.user.email
    subject = 'Статус вашего заказа изменился'
    html_content = render_to_string(
        template_name='email/order_status_changed.html',
        context={
            'pk': order_id,
            'status': new_status
        }
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user_email],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def order_created_email(order_id):
    order = Order.objects.get(pk=order_id)
    user_email = order.user.email
    subject = 'Ваш заказ принят'
    html_content = render_to_string(
        template_name='email/order_created.html',
        context={
            'pk': order_id
        }
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user_email],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()