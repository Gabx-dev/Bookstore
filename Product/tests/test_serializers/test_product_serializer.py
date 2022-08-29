from django.test import TestCase

from Product.factories import ProductFactory, CategoryFactory
from Product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self):
        productTitle = "Mouse"
        price = 100

        self.category = [CategoryFactory()]
        self.product = ProductFactory(
            title=productTitle, price=price, category=self.category
        )
        self.product_serializer = ProductSerializer(self.product)

    def test_product_serializer(self):
        serialized_data = self.product_serializer.data
        self.assertEqual(serialized_data["title"], self.product.title)
        self.assertEqual(serialized_data["price"], self.product.price)
        self.assertEqual(
            serialized_data["category"][0]["title"], self.category[0].title
        )
