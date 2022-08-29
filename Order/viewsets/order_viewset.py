from rest_framework.viewsets import ModelViewSet

from Order.models import Order
from Order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
