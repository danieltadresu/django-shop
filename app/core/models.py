from django.db import models

# Create your models here.

class Category(models.Model):
    title       = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Product(models.Model):
    title       = models.CharField(max_length=30)
    price       = models.IntegerField()
    description = models.CharField(max_length=60)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='products', null=True)

    def __str__(self):
        return self.title
