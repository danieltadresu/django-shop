from django.urls import path
from core.views import getIndex, registro

urlpatterns = [
    path('', getIndex, name='getIndex'),
    path('registro/', registro, name='registro')
]
