from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KRKB4CoeqQ5d4a5itssPnca5uQ6aZOq3ZnPfZWHSxLVqwMYsvIC82Lpeo0Vu6FhTE0YjX5BUrEqwW4eFM3Tb0XS00Mtk52W4c',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)