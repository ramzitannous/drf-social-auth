from rest_framework.views import APIView
from drf_social.serializers import SocialInputSerializer
from drf_social.helpers import load_providers

load_providers()

class SocialLoginView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self):
        token_serializer = SocialInputSerializer(data=self.request.data)
        token_serializer.is_valid(raise_exception=True)


