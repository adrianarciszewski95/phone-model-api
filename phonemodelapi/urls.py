from django.urls import include, path
from rest_framework import routers
from phonemodelapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'phoneimages', views.PhoneImageViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'operatingsystems', views.OperatingSystemViewSet)
router.register(r'phones', views.PhoneViewSet)
router.register(r'ratings', views.RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

