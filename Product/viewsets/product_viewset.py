from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated

from Product.models import Product
from Product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    authentication_classes = [
        BasicAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("id")
