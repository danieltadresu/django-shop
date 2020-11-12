from django.shortcuts import render


from core.models import (
    Product,
    Order
)

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib.auth.models import (
    User,
    Group
)

import stripe
stripe.api_key = 'sk_test_51HQlYBKVWRemJMNbYdPyEEGInMoFLN9MwF1UA0m6rxk8o97VVB4jS5B4LXBjNN8XGeVXWiBjcNTT1NqIin9I1HJj00LtxiIU4C'

def getIndex(request):
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts
    }
    return render(request, 'index.html', data)

def getAddProduct(request):
    return render(request, 'products/add-product.html')

def postAddToBag(request):
    return render(request, 'index.html')

#Views to login and authentication
def getLogIn(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/login.html')
    return render(request, 'index.html')

def getLogOut(request):
    logout(request)
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts
    }
    return render(request, 'index.html', data)

def postLogIn(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        data = {
            'check' : False
        }
        return render(request, 'auth/login.html', data)
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts
    }
    return render(request, 'index.html', data)

def getSignUp(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/signup.html')
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts
    }
    return render(request, 'index.html', data)

def postSignUp(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    user = authenticate(request, username=username, password=password)
    user_group = Group.objects.get(name='Clients')
    user.groups.add(user_group)
    login(request, user)
    return render(request, 'auth/signup.html')
# end

# Views to Stripe payments
def getCheckout(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/login.html')
    return render(request, 'shop/checkout.html')

    #product = Product.objects.get(productId=id)
    #checkout_session = stripe.checkout.Session.create(
    #    payment_method_types=['card'],
    #    line_items=[
    #        {
    #          'price_data': {
    #            'currency': 'clp',
    #            'unit_amount': product.price,
    #            'product_data': {
    #              'name': product.title,
    #             },
    #           },
    #             'quantity': 1,
    #         },
    #        ],
    #        mode='payment',
    #        success_url='http://localhost:8000/success/' + str(id),
    #        cancel_url='http://localhost:8000',
    #    )
    #return render(request, 'shop/checkout.html', {'id': checkout_session.id})

def getSuccessPay(request, id):
    fetchProduct = Product.objects.get(productId=id)
    current_user = request.user
    Order.objects.create(
        product = fetchProduct,
        total_price = fetchProduct.price,
        user = current_user
    )
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts
    }
    return render(request, 'index.html', data)
# end
