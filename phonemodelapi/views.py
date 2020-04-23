from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.http import HttpResponseNotAllowed
from rest_framework import permissions
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import PhoneSerializer, PhoneBasicSerializer, ProfileSerializer, RatingSerializer,  BrandSerializer, \
    UserSerializer
from .models import Phone, Profile, Rating, Brand


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


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
    ordering_fields = ['brand__name', 'name', 'year']
    ordering = ['brand__name', 'name']
    pagination_class = PhoneSetPagination
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminOrReadOnly,)

    @action(detail=False, methods=['get'])
    def basic(self, request, **kwargs):
        queryset = Phone.objects.all().order_by('brand__name', 'name')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PhoneBasicSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    @action(detail=True, methods=['POST'])
    def rate_phone(self, request, pk=None):
        phone = Phone.objects.get(id=pk)
        user = request.user
        author = Profile.objects.get(id=user.id)
        if 'stars' in request.data:
            stars = request.data['stars']
            if 'opinion' in request.data:
                opinion = request.data['opinion']
                Rating.objects.create(phone=phone, author=author, stars=stars, opinion=opinion)
                response = {'message': 'Rating created'}
                return Response(response, status=status.HTTP_200_OK)
            else:
                Rating.objects.create(phone=phone, author=author, stars=stars)
                response = {'message': 'Rating created'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PUT'])
    def edit_rating(self, request, pk=None):
        phone = Phone.objects.get(id=pk)
        user = request.user
        author = Profile.objects.get(id=2)
        if 'stars' and 'opinion' in request.data:
            stars = request.data['stars']
            opinion = request.data['opinion']
            rating = Rating.objects.get(phone=phone.id, author=author.id)
            rating.opinion = opinion
            rating.stars = stars
            rating.save()
            response = {'message': 'Rating updated'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'No data in request'}
            return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['DELETE'])
    def delete_rating(self, request, pk=None):
        phone = Phone.objects.get(id=pk)
        user = request.user
        author = Profile.objects.get(id=user.id)
        rating = Rating.objects.get(phone=phone.id, author=author.id)
        self.perform_destroy(rating)
        response = {'message': 'Rating deleted'}
        return Response(response, status=status.HTTP_200_OK)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RatingSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['date', 'stars']
    ordering = ['-date']
    pagination_class = RatingSetPagination
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        phone = self.request.query_params.get('phone', None)
        author = self.request.query_params.get('author', None)

        if phone and not author:
            return Rating.objects.filter(phone=phone)
        if author and not phone:
            return Rating.objects.filter(user=author)
        else:
            return Rating.objects.none()

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You cant delete rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrReadOnly,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data['name']
        instance.logo = request.data['logo']
        instance.save()
        response = {'message': 'Brand updated'}
        return Response(response, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        number_of_phones = instance.number_of_phones()
        if number_of_phones == 0:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponseNotAllowed("Method not allowed")


