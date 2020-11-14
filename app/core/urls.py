from django.urls import path

from core.views import (
    getIndex,
    getAddProduct,
    postAddToBag,
    getLogIn,
    postLogIn,
    getLogOut,
    getSignUp,
    postSignUp,
    getCheckout,
    getSuccessPay,
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('admin/add-product', getAddProduct, name='addProduct'),
    path('add-to-bag/<int:id>', postAddToBag, name='postAddToBag'),
    path('login/', getLogIn, name='getLogIn'),
    path('login-auth/', postLogIn, name='postLogIn'),
    path('logout/', getLogOut, name='getLogOut'),
    path('signup/', getSignUp, name='getSignUp'),
    path('signup-auth/', postSignUp, name='postSignUp'),
    path('checkout/', getCheckout, name='checkout'),
    path('success/<int:id>', getSuccessPay, name='success'),
]
