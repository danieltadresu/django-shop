from django.urls import path

from core.views import (
    getIndex,
    getSignup,
    getCheckout,
    getSuccessPay,
    getAddProduct
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('checkout/product/<int:id>', getCheckout, name='checkout'),
    path('success/<int:id>', getSuccessPay, name='success'),
    path('registro/', getSignup, name='registro'),
    path('admin/add-product', getAddProduct, name='add-product'),
]
