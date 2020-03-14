from django.test import TestCase

# My libs
from apps.authorization.models import Services, LdapSettings


class ServicesModelsTest(TestCase):
    def setUp(self):
        self.services_attributes = \
            {
                'name': 'test_one_services',
            }

        self.services = Services.objects.create(
            **self.services_attributes)

    def test_contains_expected_fields(self):
        self.assertTrue(hasattr(self.services, 'name'))
        self.assertTrue(hasattr(self.services, 'token'))

    def test_type_model_fields(self):
        self.assertTrue(
            self.services._meta.get_field('name').get_internal_type(),
            'CharField'
        )
        self.assertTrue(
            self.services._meta.get_field('token').get_internal_type(),
            'CharField'
        )


class LdapSettingsModelsTest(TestCase):
    def setUp(self):
        self.settings_attributes = \
            {
                'name': 'test_one_ldap_settings',
            }

        self.settings_ldap = LdapSettings.objects.create(
            **self.settings_attributes)

    def test_contains_expected_fields(self):
        self.assertTrue(hasattr(self.settings_ldap, 'name'))
        self.assertTrue(hasattr(self.settings_ldap, 'settings'))

        self.assertEqual(set(self.settings_ldap.settings[0].keys()),
                         {
                            'LDAP_URL',
                            'LDAP_SEARCH_BASE'
                         }
        )

    def test_type_model_fields(self):
        self.assertTrue(
            self.settings_ldap._meta.get_field('name').get_internal_type(),
            'CharField'
        )
        self.assertTrue(
            self.settings_ldap._meta.get_field('settings').get_internal_type(),
            'JSONField'
        )