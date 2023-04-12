from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'iot'

urlpatterns = [
    path('mqtt/', TemplateView.as_view(template_name='iot/mqtt.html')),
    path('upload/', upload, name = 'upload'),
    path('sec_file/', SecFileListView.as_view(), name = 'list')
]
