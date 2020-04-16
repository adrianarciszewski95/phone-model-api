from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly
from .serializers import UserSerializer, PhoneSerializer, PhoneBasicSerializer, ProfileSerializer
from .models import Phone, Profile
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# class PhoneImageViewSet(viewsets.ModelViewSet):
#     queryset = PhoneImage.objects.all()
#     serializer_class = PhoneImageSerializer
#
#
# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

class PhoneSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'


class PhoneFilter(filters.FilterSet):
    year_min = filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_max = filters.NumberFilter(field_name='year', lookup_expr='lte')
    display_diagonal_min = filters.NumberFilter(field_name='display_diagonal', lookup_expr='gte')
    display_diagonal_max = filters.NumberFilter(field_name='display_diagonal', lookup_expr='lte')
    processor_clock_min = filters.NumberFilter(field_name='processor_clock', lookup_expr='gte')
    processor_clock_max = filters.NumberFilter(field_name='processor_clock', lookup_expr='lte')
    processor_cores_min = filters.NumberFilter(field_name='processor_cores', lookup_expr='gte')
    processor_cores_max = filters.NumberFilter(field_name='processor_cores', lookup_expr='lte')
    internal_memory_min = filters.NumberFilter(field_name='internal_memory', lookup_expr='gte')
    internal_memory_max = filters.NumberFilter(field_name='internal_memory', lookup_expr='lte')
    ram_memory_min = filters.NumberFilter(field_name='ram_memory', lookup_expr='gte')
    ram_memory_max = filters.NumberFilter(field_name='ram_memory', lookup_expr='lte')
    battery_capacity_min = filters.NumberFilter(field_name='battery_capacity', lookup_expr='gte')
    battery_capacity_max = filters.NumberFilter(field_name='battery_capacity', lookup_expr='lte')
    back_camera_resolution_min = filters.NumberFilter(field_name='back_camera_resolution', lookup_expr='gte')
    back_camera_resolution_max = filters.NumberFilter(field_name='back_camera_resolution', lookup_expr='lte')
    back_camera_amount_min = filters.NumberFilter(field_name='back_camera_amount', lookup_expr='gte')
    back_camera_amount_max = filters.NumberFilter(field_name='back_camera_amount', lookup_expr='lte')
    front_camera_resolution_min = filters.NumberFilter(field_name='front_camera_resolution', lookup_expr='gte')
    front_camera_resolution_max = filters.NumberFilter(field_name='front_camera_resolution', lookup_expr='lte')

    class Meta:
        model = Phone
        fields = ['brand__name', 'year_min', 'year_max', 'display_diagonal_min', 'display_diagonal_max',
                  'operating_system', 'processor_clock_min', 'processor_clock_max', 'processor_cores_min',
                  'processor_cores_max', 'internal_memory_min', 'internal_memory_max', 'ram_memory_min',
                  'ram_memory_max', 'memory_card_slot', 'battery_capacity_min', 'battery_capacity_max',
                  'battery_removable', 'quick_battery_charging', 'wireless_battery_charging',
                  'back_camera_resolution_min', 'back_camera_resolution_max', 'back_camera_amount_min',
                  'back_camera_amount_max', 'front_camera_resolution_min', 'front_camera_resolution_max', 'sim_size',
                  'dual_sim', 'e_sim', 'audio_jack', 'bluetooth_version', 'fingerprint', 'nfc', 'usb_type']


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PhoneFilter
    search_fields = ['^name', '^brand__name']
    ordering_fields = ['brand__name', 'name', 'year'] #need average_rating and number_of_ratings
    ordering = ['brand__name', 'name']
    pagination_class = PhoneSetPagination
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrReadOnly,)

    # get basic information from model Phone
    @action(detail=False, methods=['get'])
    def basic(self, request, **kwargs):
        queryset = Phone.objects.all().order_by('brand__name', 'name')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PhoneBasicSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.annotate()


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
