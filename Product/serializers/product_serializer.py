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

  category = CategorySerializer(read_only=True, many=True)
  categories_id = serializers.PrimaryKeyRelatedField(
    queryset=Category.objects.all(), write_only=True, many=True
  )
