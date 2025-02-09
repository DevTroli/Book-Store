from rest_framework import serializers

from product.models.category import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
        ]
