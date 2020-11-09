from django.urls import path

from core.views import (
    getIndex,
    registro,
    getCheckout,
    getSuccessPay
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('checkout/product/<int:id>', getCheckout, name='checkout'),
    path('success/', getSuccessPay, name="success"),
    path('registro/', registro, name='registro'),
]
