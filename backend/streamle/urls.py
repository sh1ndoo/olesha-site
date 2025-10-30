from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RandomStreamView


urlpatterns = [
    path('random_stream', RandomStreamView.as_view(), name='random_stream'),
]