from rest_framework import routers
from api.views import  DetectFileViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('/detect', DetectFileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
