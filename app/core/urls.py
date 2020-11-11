from django.urls import path

from core.views import (
    getIndex,
    getAuthLogIn,
    postAuthLogIn,
    getSignup,
    getCheckout,
    getSuccessPay,
    getAddProduct
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('login/', getAuthLogIn, name='getAuthLogIn'),
    path('login/auth/', postAuthLogIn, name='postAuthLogIn'),

    ##

    path('checkout/product/<int:id>', getCheckout, name='checkout'),
    path('success/<int:id>', getSuccessPay, name='success'),
    path('registro/', getSignup, name='registro'),
    path('admin/add-product', getAddProduct, name='add-product'),
]
