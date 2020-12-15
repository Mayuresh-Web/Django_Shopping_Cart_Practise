from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False, default='')
    phone_no = models.IntegerField()
    age = models.IntegerField(default=0)


class Product(models.Model):
    product_name = models.CharField(max_length=1000)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    our_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.TextField()


class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, related_name="user_cart", on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
