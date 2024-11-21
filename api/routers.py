from rest_framework.routers import DefaultRouter, SimpleRouter

from api.views import ActionViewSet

router = DefaultRouter()

router.register('actions', ActionViewSet, basename='actions')

urlpatterns = router.urls

