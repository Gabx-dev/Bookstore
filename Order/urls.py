from django.urls import include, path
from rest_framework import routers

from Order import viewsets


router = routers.SimpleRouter()
router.register("order", viewsets.OrderViewSet, basename="order")

urlpatterns = [path("", include(router.urls))]
