from rest_framework import serializers
from drf_social import models

try:
    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
except ImportError:
    raise ImportError("must install rest_framework_simplejwt first")

class SocialInputSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=100)
    provider = serializers.ChoiceField(choices=(for (p,p) in models.Providers))


class JWTResponseSerializer(TokenObtainPairSerializer):
    pass