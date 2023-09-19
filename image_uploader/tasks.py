from celery import shared_task
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from .models import UploadedImage

@shared_task
def generate_thumbnail_task(image_id, height):
    uploaded_image = UploadedImage.objects.get(id=image_id)

    # Open the original image
    original_image = Image.open(uploaded_image.image)
    original_image.thumbnail((height, height))

    # Create a thumbnail image
    thumbnail_io = BytesIO()
    original_image.save(thumbnail_io, format='JPEG')

    # Save the thumbnail to the corresponding field
    if height == 200:
        uploaded_image.thumbnail_200.save('thumbnail_200.jpg', ContentFile(thumbnail_io.getvalue()), save=False)
    elif height == 400:
        uploaded_image.thumbnail_400.save('thumbnail_400.jpg', ContentFile(thumbnail_io.getvalue()), save=False)

    uploaded_image.save()

    return f'Thumbnails generated for image {image_id}'
