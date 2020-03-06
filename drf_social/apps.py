from django.apps import AppConfig

class SocialAuthConfig(AppConfig):
    name = 'drf_social'

    def ready(self):
        from drf_social.helpers import load_providers
        load_providers()
