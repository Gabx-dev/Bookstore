from rest_framework import serializers

from Order.models import Order
from Product.models import Product
from Product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ['product', 'total', 'user', 'product_id', ]

  product = ProductSerializer(read_only=True, many=True)
  product_id = serializers.PrimaryKeyRelatedField(
    queryset=Product.objects.all(), write_only=True, many=True
  )
  total = serializers.SerializerMethodField()

  def get_total(self, instance):
    return sum([product.price for product in instance.product.all()])