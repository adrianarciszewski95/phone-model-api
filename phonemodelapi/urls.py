from django.urls import include, path
from rest_framework import routers
from phonemodelapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'phones', views.PhoneViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'ratings', views.RatingViewSet, basename="ratings")


urlpatterns = [
    path('', include(router.urls)),
]

