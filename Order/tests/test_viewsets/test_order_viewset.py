import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from Order.factories import OrderFactory, UserFactory
from Order.models import Order
from Product.factories import ProductFactory, CategoryFactory
from Order.models import Order


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(category=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        res = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        data = json.loads(res.content)

        self.assertEqual(data[0]["product"][0]["title"], self.product.title)

        self.assertEqual(data[0]["product"][0]["price"], self.product.price)

        self.assertEqual(data[0]["product"][0]["active"], self.product.active)

        self.assertEqual(
            data[0]["product"][0]["category"][0]["title"], self.category.title
        )

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()

        data = json.dumps({"products_id": [product.id], "user": user.id})

        res = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)
