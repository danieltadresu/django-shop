from django.urls import path

from core.views import (
    getIndex,
    getAddProduct,
    getCart,
    postAddToCart,
    getLogIn,
    postLogIn,
    getLogOut,
    getSignUp,
    postSignUp,
    getSuccessPay,
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('admin/add-product', getAddProduct, name='addProduct'),
    path('cart/', getCart, name='cart'),
    path('add-to-cart/<int:id>', postAddToCart, name='postAddToCart'),
    path('login/', getLogIn, name='getLogIn'),
    path('login-auth/', postLogIn, name='postLogIn'),
    path('logout/', getLogOut, name='getLogOut'),
    path('signup/', getSignUp, name='getSignUp'),
    path('signup-auth/', postSignUp, name='postSignUp'),
    path('success/<int:id>', getSuccessPay, name='success'),
]
