from rest_framework.viewsets import ModelViewSet
from Product.models import Product
from Product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("id")
