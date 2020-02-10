from django.shortcuts import render, get_object_or_404

from .models import Product, Category
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'categories': categories,
                                                      'products': products,
                                                      'category': category})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'product_form': product_form})
