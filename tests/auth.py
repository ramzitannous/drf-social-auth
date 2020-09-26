from rest_framework.test import APITestCase

class FaceBookTest(APITestCase):

    def test_authenticate(self):
        res = self.client.post("social/login", data={
            "provider": "FACEBOOK",
            "access_token": ""})
