from django.urls import path

from core.views import (
    getIndex,
    getAuthLogIn,
    postAuthLogIn,
    getCheckout,
    getSuccessPay,
    getAddProduct
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('login/', getAuthLogIn, name='getAuthLogIn'),
    path('auth/', postAuthLogIn, name='postAuthLogIn'),

    ##

    path('checkout/product/<int:id>', getCheckout, name='checkout'),
    path('success/<int:id>', getSuccessPay, name='success'),
    path('admin/add-product', getAddProduct, name='add-product'),
]
