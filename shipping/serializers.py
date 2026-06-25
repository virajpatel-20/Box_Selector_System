from rest_framework import serializers
from .models import Product, Box, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_name",
            "quantity"
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        source="orderitem_set",
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "created_at",
            "items"
        ]