from django.test import TestCase

from Product.factories import CategoryFactory
from Product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
  def setUp(self):
    self.category = CategoryFactory()
    self.category_serializer = CategorySerializer(self.category)

  def test_category_serializer(self):
    serialized_data = self.category_serializer.data

    self.assertEqual(serialized_data['title'], self.category.title)