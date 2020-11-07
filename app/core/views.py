from django.shortcuts import render
from core.models import Product
from core.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def getIndex(request):
    fetchAllProducts = Product.objects.all()
    data = {
        'products': fetchAllProducts
    }
    return render(request, 'index.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return render(request, 'index.html', data)
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)
