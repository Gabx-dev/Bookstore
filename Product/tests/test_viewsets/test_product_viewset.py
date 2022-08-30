import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from Product.factories import ProductFactory, CategoryFactory
from Product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(category=[self.category])

    def test_product(self):
        res = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        data = json.loads(res.content)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertEqual(data[0]["id"], self.product.id)

        self.assertEqual(data[0]["title"], self.product.title)

        self.assertEqual(data[0]["description"], self.product.description)

        self.assertEqual(data[0]["price"], self.product.price)

        self.assertEqual(data[0]["active"], self.product.active)

        self.assertEqual(data[0]["category"][0]["title"], self.category.title)

        self.assertEqual(
            data[0]["category"][0]["description"], self.category.description
        )

        self.assertEqual(data[0]["category"][0]["active"], self.category.active)

    def test_create_product(self):
        category = CategoryFactory()

        product = {
            "title": "1984",
            "description": "",
            "price": 1984,
            "active": True,
            "categories_id": [category.id],
        }

        data = json.dumps(product)

        res = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title=product["title"])
