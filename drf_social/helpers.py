import json
import django.conf as conf

from drf_social.models import AuthProvider, Providers


def extract_scopes(scopes):
    try:
        scopes = json.loads(scopes)
        return scopes
    except json.JSONDecodeError:
        raise ValueError("Invalid extras were provided, must be json encoded")


AUTH_MAPPING = {
    Providers.GOOGLE: "GOOGLE_OAUTH2",
    Providers.FACEBOOK: "FACEBOOK"
}


def load_providers():
    all_auth = AuthProvider.objects.all()
    for auth in all_auth:
        setattr(conf.settings, f"SOCIAL_AUTH_{AUTH_MAPPING[auth.provider]}_KEY", auth.client_id)
        setattr(conf.settings, f"SOCIAL_AUTH_{AUTH_MAPPING[auth.provider]}_SECRET", auth.client_secret)
        setattr(conf.settings, f"SOCIAL_AUTH_{AUTH_MAPPING[auth.provider]}_SCOPE", extract_scopes(auth.scopes))
