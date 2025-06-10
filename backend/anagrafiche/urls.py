from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, FornitoreViewSet

router = DefaultRouter()
router.register(r'clienti', ClienteViewSet)
router.register(r'fornitori', FornitoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
