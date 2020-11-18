from django.urls import path

from core.views import (
    getIndex,
    getProducts,
    getProductsFiltered,
    getAdminProducts,
    postAddProduct,
    postDeleteProduct,
    getCart,
    postCartAddItem,
    postCartDeleteItem,
    getOrder,
    postOrder,
    getLogIn,
    postLogIn,
    getLogOut,
    getSignUp,
    postSignUp
)

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('products/', getProducts, name='getProducts'),
    path('filtered-products/<int:id>', getProductsFiltered, name='getProductsFiltered'),
    path('admin-products/', getAdminProducts, name='getAdminProducts'),
    path('create-product/', postAddProduct, name='addProduct'),
    path('delete-product/<int:id>', postDeleteProduct, name='postDeleteProduct'),
    path('cart/', getCart, name='cart'),
    path('cart-add-item/<int:id>', postCartAddItem, name='postCartAddItem'),
    path('cart-delete-item/<int:id>', postCartDeleteItem, name='postCartDeleteItem'),
    path('create-order/', getOrder, name='getOrder'),
    path('checkout/<slug:id>', postOrder, name='postOrder'),
    path('login/', getLogIn, name='getLogIn'),
    path('login-auth/', postLogIn, name='postLogIn'),
    path('logout/', getLogOut, name='getLogOut'),
    path('signup/', getSignUp, name='getSignUp'),
    path('signup-auth/', postSignUp, name='postSignUp'),
]
