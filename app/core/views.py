from django.shortcuts import render

from core.models import Product
from core.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

import stripe
stripe.api_key = 'sk_test_51HQlYBKVWRemJMNbYdPyEEGInMoFLN9MwF1UA0m6rxk8o97VVB4jS5B4LXBjNN8XGeVXWiBjcNTT1NqIin9I1HJj00LtxiIU4C'

def getIndex(request):
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts
    }

    return render(request, 'index.html', data)

def getCheckout(request, id):
    product = Product.objects.get(productId=id)
    print('My product -> ', product.price )
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'clp',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.title,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8001/success/',
            cancel_url='http://localhost:8001',
        )

    return render(request, 'products/checkout-products.html', {'id': checkout_session.id})

def getSuccessPay(request):
    print('hola!')
    return render(request, 'index.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return render(request, 'index.html', data)
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)
