import factory

from Product.models import Product
from .category_factory import CategoryFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    price = factory.Faker("pyint")
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker("pystr")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
