from rest_framework import serializers

from Product.models.product import Category, Product
from Product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]

    extra_kwargs = {"category": {"required": False}}

    category = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    def create(self, validated_data):
        category_data = validated_data.pop("categories_id")

        product = Product.objects.create(**validated_data)

        for category in category_data:
            product.category.add(category)

        return product
