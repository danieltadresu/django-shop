from django import forms
from core.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

#class ProductForm(forms.ModelForm):
#
#    class Meta:
#        model = Product
#        fields = [
#            'productId',
#            'title',
#            'price',
#            'description',
#            'image',
#            'category',
#            'band'
#        ]
