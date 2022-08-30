from django.test import TestCase

from Order.factories import OrderFactory, ProductFactory
from Order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.products = [ProductFactory() for _ in range(2)]
        self.order = OrderFactory(product=self.products)
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEqual(serializer_data["product"][0]["title"], self.products[0].title)
        self.assertEqual(serializer_data["product"][1]["title"], self.products[1].title)
