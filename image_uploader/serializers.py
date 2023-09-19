from rest_framework import serializers
from .models import UserProfile, UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['id', 'thumbnail_200', 'thumbnail_400', 'image']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'account_tier']
