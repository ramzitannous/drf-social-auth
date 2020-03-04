from rest_framework.test import APITestCase

class FaceBookTest(APITestCase):

    def test_authenticate(self):
        res = self.client.post("social/login", data={
            "provider": "FACEBOOK",
            "access_token": "EAAFm5syZAZCy4BAIjyNBfGuL1HQA8RqtkxqXBGaCotchdSNktRhvpKIyY5vR5V0gIRQK4NpjWHbMHMiBUzI4ml2S388Y7j7YVfPORO7mqDQrRDJ55DqtPRnYnFG99ojbrpzYF4gDkWZBZA7groiZCteZCbTdgrbZBcbuQXZCz3QG3jw6TUTxdhMW"
        })