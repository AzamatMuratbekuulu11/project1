from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=16,unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    user = models.CharField(max_length=32)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.product}'
