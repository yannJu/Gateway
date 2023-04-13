from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', KakaoLoginView.as_view()),
    path('oauth', KakaoAuthView.as_view(), name="oatuh"),
]
