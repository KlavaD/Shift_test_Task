from django.urls import include, path
from rest_framework import routers

from api.views import SalaryViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'salary', SalaryViewSet, basename='salary')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]
