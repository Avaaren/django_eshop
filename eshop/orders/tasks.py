from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    # order = Order.objects.get(id=order_id)
    # subject = 'Order № {}'.format(order.id)
    # message = '{},\n Your order succesfully added.\n\
    #     Your order`s id {}'.format(order.first_name, order.id)
    mail_sent = send_mail('subject', 'message', 'admin@mail.ru', ['ex@gmail.com', ])

    return mail_sent
