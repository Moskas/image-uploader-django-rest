from django.apps import AppConfig

default_app_config = 'image_uploader.ImageUploaderConfig'

class ImageUploaderConfig(AppConfig):
    name = 'image_uploader'

    def ready(self):
        import image_uploader.signals
