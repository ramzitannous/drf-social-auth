from django.http import HttpResponse
from rest_framework.views import APIView
from social_django.utils import load_strategy, Strategy, load_backend

from drf_social.serializers import SocialInputSerializer

class SocialLoginView(APIView):
    permission_classes = []
    authentication_classes = []
    _strategy: Strategy

    def post(self, *args, **kwargs):
        token_serializer = SocialInputSerializer(data=self.request.data)
        token_serializer.is_valid(raise_exception=True)
        self._strategy = load_strategy(self.request)
        backend = load_backend(self._strategy, token_serializer.data["provider"].lower(), '/')
        return HttpResponse()
