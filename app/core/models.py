from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    categoryId  = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Band(models.Model):
    bandId      = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Product(models.Model):
    productId   = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=30)
    price       = models.IntegerField()
    description = models.CharField(max_length=60)
    image       = models.ImageField(upload_to='products', null=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    band        = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Client(models.Model):
    rut         = models.CharField(primary_key=True, max_length=11)
    name        = models.CharField(max_length=30)
    lastName    = models.CharField(max_length=30)

    def __str__(self):
        return self.rut

class Order(models.Model):
    orderId      = models.IntegerField(primary_key=True)
    total_price  = models.IntegerField(null=True)
    user         = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.orderId)

class OrderItem(models.Model):
    orderItemId = models.IntegerField(primary_key=True)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    order       = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.orderItemId)



class Vehiculo():
    def __init__(self, marca,modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__estado = True
        self.__items = []

    def agregar(self, colores):
        self.__items.append(colores)

    def arrancar(self):
        if(self.__estado == "False"):
            self.__estado == True

    def getMarca(self):
        return self.__marca

    def setMarca(self,marca):
        self.__marca = marca

    def getModelo(self):
        return self.__modelo

    def setModelo(self,modelo):
        self.__modelo = modelo

    def __str__(self):
        return "Marca: " + self.__marca + " | Modelo: " + self.__modelo + " | " + str(self.__items)
