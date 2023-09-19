from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .tasks import generate_thumbnail_task

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_image(request):
    # Logic to handle image uploading based on account tier
    # This includes generating thumbnails and handling expiration
    # Update the `image` variable below with your actual upload logic

    account_tier = request.user.userprofile.account_tier
    image = request.data.get('image')

    # Example: Saving the uploaded image and creating thumbnails
    uploaded_image = UploadedImage.objects.create(user=request.user, image=image)

    # TODO: Generate thumbnails and expiration links based on the account tier

    serializer = UploadedImageSerializer(uploaded_image)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_images(request):
    user = request.user
    images = UploadedImage.objects.filter(user=user)
    serializer = UploadedImageSerializer(images, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
