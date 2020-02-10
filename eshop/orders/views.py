from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderForm(data=request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'orders/order/create.html', {'form': form})
