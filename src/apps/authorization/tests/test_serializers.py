from django.test import TestCase

# My libs
from apps.authorization.serializers import AuthSerializer


class AuthSerializerTest(TestCase):
    def setUp(self):
        self.auth_attributes = \
            {
                'username': 'username',
                'password': 'password',
                'token': 'token',
            }

        self.serializer = AuthSerializer(self.auth_attributes)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()),
                         {
                             'username',
                             'password',
                             'token'
                         })
