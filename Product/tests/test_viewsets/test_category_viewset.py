import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from Product.factories import CategoryFactory
from Product.models import Category


class TestCategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory()

    def test_category(self):
        res = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        data = json.loads(res.content)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(data["results"][0]["title"], self.category.title)
        self.assertEqual(data["results"][0]["description"], self.category.description)
        self.assertEqual(data["results"][0]["active"], self.category.active)

    def test_create_category(self):
        category = {"title": "Technology", "description": "", "active": True}

        data = json.dumps(category)

        res = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title=category["title"])
