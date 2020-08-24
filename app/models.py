from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=3, validators=[
                                MinValueValidator(0.0)])
    img = models.ImageField()
    stock = models.PositiveIntegerField()
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    area = models.CharField(max_length=150)
    street = models.CharField(max_length=200)
    block = models.CharField(max_length=50)
    optional = models.CharField(max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField()


class Order(models.Model):
    STATUS = [
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
        ("Pending", "Pending"),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS, default="Pending")
    order_ref = models.CharField(max_length=10)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='address')
    date_time = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=3, validators=[
                                MinValueValidator(0.0)])

    def __str__(self):
        return ("Order: " + self.order_ref)


class Basket(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='baskets')


@receiver(post_save, sender=Basket)
def reduce_inventory(instance, created, **kwargs):
    if created:
        product = Product.objects.get(id=instance.product.id)
        product.stock -= instance.quantity
        product.save()
