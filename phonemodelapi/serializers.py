from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brand, Phone, Rating, Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'last_name', 'first_name', 'date_joined']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'phone', 'author', 'stars', 'opinion', 'date']


class PhoneSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, required=False)

    class Meta:
        model = Phone
        fields = ['id', 'name', 'brand', 'name_with_brand', 'year', 'photo', 'display_diagonal', 'operating_system',
                  'processor_clock', 'processor_cores', 'internal_memory', 'ram_memory', 'memory_card_slot',
                  'battery_capacity', 'battery_removable', 'quick_battery_charging', 'wireless_battery_charging',
                  'back_camera_resolution', 'back_camera_amount', 'front_camera_resolution', 'sim_size', 'dual_sim',
                  'e_sim', 'audio_jack', 'bluetooth_version', 'fingerprint', 'nfc', 'usb_type',
                  'additional_information', 'ratings', 'number_of_ratings', 'average_rating']


class PhoneBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'name_with_brand', 'photo',  'average_rating']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'photo', 'favourite_brand', 'favourite_phone', 'address', 'city', 'country', 'ratings',
                  'number_of_ratings']


class BrandSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, required=False)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo', 'number_of_phones', 'phones']




