from django.db import models

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
    orderId      = models.AutoField(primary_key=True)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price  = models.IntegerField(null=True)
    #client      = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orderId)
