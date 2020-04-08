from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import PhoneImage, Brand, OperatingSystem, Phone, Rating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PhoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneImage
        fields = ['id', 'photo']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo', 'number_of_phones']


class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = ['id', 'name']


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'name', 'main_photo', 'phone_images', 'brand', 'year', 'display_diagonal', 'operating_system',
                  'processor_clock', 'processor_cores', 'internal_memory', 'ram_memory', 'memory_card_slot',
                  'battery_capacity', 'battery_removable', 'quick_battery_charging', 'wireless_battery_charging',
                  'back_camera_resolution', 'back_camera_amount', 'front_camera_resolution', 'sim_size', 'dual_sim',
                  'e_sim', 'audio_jack', 'bluetooth_version', 'fingerprint', 'nfc', 'usb_type',
                  'additional_information', 'name_with_brand', 'number_of_ratings', "average_rating"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'phone', 'user', 'stars', 'opinion']

