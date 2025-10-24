from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScranViewSet, TagListView, CountryListView

router = DefaultRouter()
router.register(r'scran', ScranViewSet, basename='scran')

urlpatterns = [
    path('', include(router.urls)),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('countries/', CountryListView.as_view(), name='country-list'),
]