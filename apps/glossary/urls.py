from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GlossaryViewSet,
)

router = DefaultRouter()
router.register(r'glossary', GlossaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
