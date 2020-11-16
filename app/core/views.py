from django.shortcuts import render

from django.http import HttpResponseRedirect

from core.models import (
    Product,
    Order,
    OrderItem
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
stripe.api_key = (
    'sk_test_51HQlYBKVWRemJMNbYdPyEEGInMoFLN9MwF1UA0m6rxk8o97VVB4jS5B4LXBjNN8XGeVXWiBjcNTT1NqIin9I1HJj00LtxiIU4C'
)

def getIndex(request):
    items = None
    selectedItems = 0
    if request.session.get('ar'):
        items = request.session.get('ar')
        selectedItems = len(items)
    else:
        pass
    fetchAllProducts = Product.objects.all()[:4]
    data = {
        'products': fetchAllProducts,
        'items': selectedItems
    }
    return render(request, 'shop/index.html', data)

def getProducts(request):
    items = None
    selectedItems = 0
    if request.session.get('ar'):
        items = request.session.get('ar')
        selectedItems = len(items)
    else:
        selectedItems = 0
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts,
        'items': selectedItems
    }
    return render(request, 'shop/product-list.html', data)

def getAddProduct(request):
    return render(request, 'products/add-product.html')

def getCart(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/login.html')
    fetchAllItems = []
    total_price = 0
    if request.session.get('ar'):
        items = request.session.get('ar')
        product = None
        index = 0
        print(items)
        for i in items:
            product = Product.objects.get(pk=items[index])
            total_price += product.price
            fetchAllItems.insert(index, product)
            index += 1
    else:
        print('No Hay sesiones!')
    data = {
        'orderItems': fetchAllItems,
        'items': len(fetchAllItems),
        'totalPrice': total_price
    }
    return render(request, 'shop/cart.html', data)

def postCartAddItem(request, id):
    if not request.user.is_authenticated:
        return render(request, 'auth/login.html')
    productsCart = 0
    if request.session.get('ar'):
        items = request.session.get('ar')
        index = len(items)
        items.insert(index + 1, id)
        request.session['ar'] = items
        productsCart = index + 1
    else:
        ar = []
        ar.insert(0, id)
        request.session['ar'] = ar
        items = request.session.get('ar')
        productsCart = 1
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def postCartDeleteItem(request, id):
    if request.session.get('ar'):
        items = request.session.get('ar')
        selectedItems = len(items)
        index = 0
        print(items)
        for i in items:
            if items[index] == id:
                items.pop(index)
                break
            index += 1
        print(items)
        request.session['ar'] = items
    else:
        print('There are not saved sessions!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def getOrder(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/login.html')
    fetchAllItems = []
    total_price = 0
    if request.session.get('ar'):
        items = request.session.get('ar')
        product = None
        index = 0
        print(items)
        for i in items:
            product = Product.objects.get(pk=items[index])
            total_price += product.price
            fetchAllItems.insert(index, product)
            index += 1
        checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
              'price_data': {
                  'currency': 'clp',
                  'unit_amount': total_price,
                  'product_data': {
                      'name': 'VINYLSMIND',
                   },
               },
               'quantity': 1,
             },
            ],
            mode='payment',
            success_url='http://localhost:8000/checkout/{CHECKOUT_SESSION_ID}',
            cancel_url='http://localhost:8000/cart',
        )
    else:
        #No hay items, el valor total es 0$ por ende no se puede realizar una orden,
        #Se retorna al index
        return HttpResponseRedirect('/')
    data = {
        'orderItems': fetchAllItems,
        'items': len(fetchAllItems),
        'totalPrice': total_price,
        'id': checkout_session.id
    }
    return render(request, 'shop/order-details.html', data)

def postOrder(request, id):
    items = request.session.get('ar')
    pay = stripe.checkout.Session.retrieve(id)
    countAllOrders = Order.objects.all().count()
    order = Order.objects.create(
        orderId = countAllOrders + 1,
        total_price = pay.amount_total,
        user = request.user
    )
    order.save()
    #Por cada Item almacenado en la sesion, registrar 1 item
    #en la tabla OrderItem
    countAllItems = OrderItem.objects.all().count() #Total de registros
    for i in items:
        countAllItems += 1
        product = Product.objects.get(pk=i)
        orderItem = OrderItem.objects.create(
            orderItemId = countAllItems,
            product = product,
            order = order,
            quantity = 1
        )
        orderItem.save()
    return render(request, 'shop/checkout.html')

#Views to login and authentication
def getLogIn(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/login.html')
    return HttpResponseRedirect('/')

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
    return HttpResponseRedirect('/')

def getSignUp(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/signup.html')
    return HttpResponseRedirect('/')

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
    return HttpResponseRedirect('/')

def getLogOut(request):
    logout(request)
    return HttpResponseRedirect('/')
# end
