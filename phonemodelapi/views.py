from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters
from .serializers import PhoneImageSerializer, BrandSerializer, ColorSerializer, OperatingSystemSerializer, \
    OSVersionSerializer, ChipsetSerializer, QuickChargeSerializer, PhoneSerializer, RatingSerializer
from .models import PhoneImage, Brand, Color, OperatingSystem, OSVersion, Chipset, QuickCharge, Phone, Rating


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class PhoneImageViewSet(viewsets.ModelViewSet):
    queryset = PhoneImage.objects.all()
    serializer_class = PhoneImageSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class OperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer


class OSVersionViewSet(viewsets.ModelViewSet):
    queryset = OSVersion.objects.all()
    serializer_class = OSVersionSerializer


class ChipsetViewSet(viewsets.ModelViewSet):
    queryset = Chipset.objects.all()
    serializer_class = ChipsetSerializer


class QuickChargeViewSet(viewsets.ModelViewSet):
    queryset = QuickCharge.objects.all()
    serializer_class = QuickChargeSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'brand__name']
    ordering_fields = ['brand__name', 'year']
    ordering = ['brand__name', 'name']


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
