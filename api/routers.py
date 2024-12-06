from rest_framework.routers import DefaultRouter, SimpleRouter

from api.views import ActionViewSet
from .api_products import ProductViewSet,CategoryViewSet

router = DefaultRouter()

router.register('actions', ActionViewSet, basename='actions')

router.register('products', ProductViewSet, basename='products')

router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls

