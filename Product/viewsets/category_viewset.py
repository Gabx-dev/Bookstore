from rest_framework.viewsets import ModelViewSet
from Product.models import Category
from Product.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("id")
