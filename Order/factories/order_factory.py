import factory

from Order.models import Order
from Product.factories import ProductFactory
from .user_factory import UserFactory


class OrderFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Order

  user = factory.SubFactory(UserFactory)

  @factory.post_generation
  def product(self, create, extracted, **kwargs):
    if not create:
      return
    
    if extracted:
      for product in extracted:
        self.product.add(product)