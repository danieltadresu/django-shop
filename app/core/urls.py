from django.urls import path

from core.views import (
    getIndex,
    getAddProduct,
    getCart,
    postCartAddItem,
    postCartDeleteItem,
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
    path('cart-add-item/<int:id>', postCartAddItem, name='postCartAddItem'),
    path('cart-delete-item/<int:id>', postCartDeleteItem, name='postCartDeleteItem'),
    path('login/', getLogIn, name='getLogIn'),
    path('login-auth/', postLogIn, name='postLogIn'),
    path('logout/', getLogOut, name='getLogOut'),
    path('signup/', getSignUp, name='getSignUp'),
    path('signup-auth/', postSignUp, name='postSignUp'),
    path('success/<int:id>', getSuccessPay, name='success'),
]
