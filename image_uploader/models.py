from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_tier = models.CharField(max_length=20, choices=[
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Enterprise', 'Enterprise')
    ])

class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploaded_images/')
    thumbnail_200 = models.ImageField(upload_to='thumbnails/200/')
    thumbnail_400 = models.ImageField(upload_to='thumbnails/400/')
    upload_datetime = models.DateTimeField(auto_now_add=True)

    def get_expiring_link(self, expiration_seconds):
        # Logic to generate an expiring link for the image
        # This can vary based on your storage backend (e.g., AWS S3, local storage)
        pass
