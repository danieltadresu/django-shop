from django.urls import path

from core.views import (
    getIndex,
    getLogIn,
    postLogIn,
    getLogOut,
    getSignUp,
    postSignUp,
    getCheckout,
    getSuccessPay,
    getAddProduct
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('login/', getLogIn, name='getLogIn'),
    path('login-auth/', postLogIn, name='postLogIn'),
    path('logout/', getLogOut, name='getLogOut'),
    path('signup/', getSignUp, name='getSignUp'),
    path('signup-auth/', postSignUp, name='postSignUp'),
    path('checkout/product/<int:id>', getCheckout, name='checkout'),
    path('success/<int:id>', getSuccessPay, name='success'),
    path('admin/add-product', getAddProduct, name='add-product'),
]
