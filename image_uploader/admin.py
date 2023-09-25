from django.contrib import admin
from .models import AccountTier, UserProfile, UploadedImage

class AccountTierAdmin(admin.ModelAdmin):
    list_display = ['name', 'thumbnail_sizes', 'original_image_link', 'expiring_links_enabled']

class UploadedImageAdmin(admin.ModelAdmin):
    actions = ['generate_expiring_links']

    def generate_expiring_links(self, request, queryset):
        for image in queryset:
            expiration_seconds = 3600  # Set a default expiration time of 1 hour
            # Call the generate_expiring_link method to get the expiring link
            expiring_link = image.generate_expiring_link(expiration_seconds)

            self.message_user(request, f'Generated expiring link for image: {expiring_link}')
    generate_expiring_links.short_description = 'Generate Expiring Links for Selected Images'


admin.site.register(AccountTier)
admin.site.register(UserProfile)
admin.site.register(UploadedImage, UploadedImageAdmin)