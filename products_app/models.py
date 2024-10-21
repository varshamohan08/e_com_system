from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name="category_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name="category_updated_by")
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name="product_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name="product_updated_by")
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name