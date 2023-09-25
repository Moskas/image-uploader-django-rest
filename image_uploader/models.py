from django.db import models
from django.contrib.auth.models import User  # Import User model
from django.core.signing import TimestampSigner
from django.utils import timezone
from datetime import timedelta

class AccountTier(models.Model):
    name = models.CharField(max_length=50)
    thumbnail_sizes = models.CharField(max_length=100, help_text="Comma-separated list of thumbnail sizes (e.g., 200,400)")
    original_image_link = models.BooleanField(default=False)
    expiring_links_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_tier = models.ForeignKey(AccountTier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.account_tier}'

class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploaded_images/')
    upload_datetime = models.DateTimeField(auto_now_add=True)

    account_tier = models.ForeignKey(AccountTier, on_delete=models.SET_NULL, null=True, blank=True)

    def generate_thumbnails(self):
        # Logic to generate thumbnails based on the account tier
        if self.account_tier:
            thumbnail_sizes = [int(size) for size in self.account_tier.thumbnail_sizes.split(',')]
            thumbnails = {}
            for size in thumbnail_sizes:
                # Assuming thumbnail URLs are generated based on the image URL
                thumbnail_url = f'{self.image.url}?size={size}'
                thumbnails[f'{size}px'] = thumbnail_url

            return thumbnails

    def generate_expiring_link(self, expiration_seconds):
        if self.image:
            # Generate the URL for the image
            image_url = self.image.url

            # Calculate the expiration time
            expiration_time = timezone.now() + timedelta(seconds=expiration_seconds)

            # Sign the URL with the expiration time
            signer = TimestampSigner()
            signed_url = signer.sign(image_url + f'?exp={int(expiration_time.timestamp())}')

            return signed_url

    def get_image_info(self):
        image_info = {}
        image_info['image'] = self.image.url
        image_info['thumbnails'] = self.generate_thumbnails()

        return image_info

    def get_expiring_link(self, expiration_seconds):
        if self.account_tier and self.account_tier.expiring_links_enabled:
            return self.generate_expiring_link(expiration_seconds)

        return None
