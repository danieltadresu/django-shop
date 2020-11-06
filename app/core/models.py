from django.db import models

# Create your models here.

class Category(models.Model):
    #categoryId  = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Product(models.Model):
    #userId      = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=30)
    price       = models.IntegerField()
    description = models.CharField(max_length=60)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
