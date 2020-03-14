from django.core.management.base import BaseCommand
from apps.authorization.models import LdapSettings
from django.db import transaction


class Command(BaseCommand):
    # TODO add domain list
    domain_list = ['DOMAIN\\', '']

    def setUpBD(self):
        for domain in self.domain_list:
            LdapSettings.objects\
                .get_or_create(name=domain,
                               settings=[{
                                "LDAP_URL": "ldaps://DOMAIN",
                                "LDAP_SEARCH_BASE": "dc=DC,dc=DC",
                                "PORT": 4321,
                                "DOMAIN": domain
                               }]
            )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.setUpBD()
        self.stdout.write(
            self.style.SUCCESS('Create all settings')
        )
