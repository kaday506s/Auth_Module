from django.test import RequestFactory, TestCase
from unittest import mock
# My libs
from apps.authorization.models import Services
from apps.authorization.views import LdapAuthViewSet


class LdapAuthViewSetTest(TestCase):
    def setUp(self):
        self.url = "/api/v1/auth"
        self.factory = RequestFactory()

        self.services_attributes = \
            {
                'name': 'test_one_services',
            }

        self.services = Services.objects.create(
            **self.services_attributes)

    def test_for_method_post(self):

        data_auth = {
                        'username': 'username',
                        'password': 'password',
                        'token': 'token',
                    }
        request = self.factory.post(
            self.url,
            data_auth,
            content_type='application/json'
        )
        view = LdapAuthViewSet.as_view({'post': 'create'})

        response = view(request).render()

        self.assertEqual(response.status_code, 403)

    def test_for_method_post_(self):

        data_auth = {
                        'username': 'username',
                        'password': 'password',
                        'token': self.services.token,
                    }
        request = self.factory.post(
            self.url,
            data_auth,
            content_type='application/json'
        )
        view = LdapAuthViewSet.as_view({'post': 'create'})

        response = view(request).render()

        self.assertEqual(response.status_code, 400)

    @mock.patch('apps.authorization.usecases.LdapBackend.get_ldap_user',
                mock.MagicMock(return_value=
                    {
                            'dn': 'dn',
                            "raw_attributes": "raw_attributes",
                            "attributes": 'attributes',
                            "raw_dn_info": "raw_dn_info",
                            "type": 'type'
                    }
                )
    )
    def test_for_method_psost_(self):

        data_auth = {
                        'username': 'username',
                        'password': 'password',
                        'token': self.services.token,
                    }
        request = self.factory.post(
            self.url,
            data_auth,
            content_type='application/json'
        )
        view = LdapAuthViewSet.as_view({'post': 'create'})

        response = view(request).render()

        self.assertEqual(response.status_code, 200)
