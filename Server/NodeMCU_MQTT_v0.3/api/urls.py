from rest_framework import routers
from api.views import  SecFileViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('/detect', SecFileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
