from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Basket, Order, Address


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ProductHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


class BasketSerializer(serializers.ModelSerializer):
    product = ProductHistorySerializer()

    class Meta:
        model = Basket
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    baskets = BasketSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "order_ref", "address",
                  "baskets", "date_time", "total"]
