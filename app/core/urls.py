from django.urls import path
from core.views import getIndex

urlpatterns = [
    path('', getIndex, name='getIndex')
]
