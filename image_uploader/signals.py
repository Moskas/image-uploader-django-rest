from django.dispatch import receiver
from django.db.models.signals import post_migrate
from .models import AccountTier
from .models import ThumbnailSize

@receiver(post_migrate)
def create_builtin_tiers(sender, **kwargs):
    """Creates built-in tiers after db migration."""
    if sender.name == 'image_uploader':
        # Initialize the BUILTIN_TIERS dictionary
        BUILTIN_TIERS = {}

        # Fetch data from the AccountTier model
        for tier in AccountTier.objects.all():
            tier_info = {
                'thumbnail_sizes': [(int(size.strip()), int(size.strip())) for size in tier.thumbnail_sizes.split(',')],
                'is_original_file': tier.original_image_link,
                'is_expiring_link': tier.expiring_links_enabled
            }
            BUILTIN_TIERS[tier.name] = tier_info

        # Print the built-in tiers for verification
        print("BUILTIN_TIERS:", BUILTIN_TIERS)

        # Rest of the code to create tiers based on BUILTIN_TIERS
        for tier_name, tier_info in BUILTIN_TIERS.items():
            if not AccountTier.objects.filter(name=tier_name).exists():
                account_tier = AccountTier.objects.create(
                    name=tier_name,
                    thumbnail_sizes=','.join(f"{size[0]},{size[1]}" for size in tier_info['thumbnail_sizes']),
                    original_image_link=tier_info['is_original_file'],
                    expiring_links_enabled=tier_info['is_expiring_link']
                )

                for width, height in tier_info['thumbnail_sizes']:
                    thumbnail_size = ThumbnailSize.objects.create(width=width, height=height)
                    account_tier.thumbnail_size.add(thumbnail_size)

                account_tier.save()
