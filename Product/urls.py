from django.urls import include, path
from rest_framework import routers

from Product import viewsets

router = routers.SimpleRouter()
router.register("product", viewsets.ProductViewSet, basename="product")
router.register("category", viewsets.CategoryViewSet, basename="category")

urlpatterns = [path("", include(router.urls))]
