from django.urls import path, include
from .views import home, reference_api_view

app_name = 'api'

urlpatterns = [
    path('', home, name='home'),
    path('reference/', reference_api_view, name='reference'),
    path('v1/', include('api.routers')),
]