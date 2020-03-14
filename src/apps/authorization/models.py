from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField
from hashlib import md5
from time import time


def random_md5():
    return md5(str(time()).encode()).hexdigest()


class Services(models.Model):
    name = models.CharField(
        max_length=256,
        null=False,
        verbose_name=_("Name"))

    token = models.CharField(
        max_length=256,
        unique=True,
        default=random_md5,
        null=False,
        verbose_name=_("token"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Services')
        verbose_name = _('Services')


def default_settings():
    return [
        {
            # ToDo Ldap settings
            "LDAP_URL": "ldaps://*****",
            "LDAP_SEARCH_BASE": "dc=***,dc=****",
            "PORT": 4321,
            "DOMAIN": "******"
         }
    ]


class LdapSettings(models.Model):
    name = models.CharField(
        max_length=32,
        null=False,
        verbose_name=_("Name"))

    settings = JSONField(
        default=default_settings,
        null=False,
        blank=True,
        verbose_name=_("Settings"))

    def __str__(self):
        return self.name


class SettingField(models.Model):
    service = models.ForeignKey(Services, models.CASCADE)

    field_ldap = models.CharField(
        max_length=128,
        null=False,
        verbose_name=_("FieldLdap"))

    description = models.CharField(
        max_length=128,
        default=None,
        blank=True,
        verbose_name=_("Description"))

    def __str__(self):
        return f"{self.service} {self.field_ldap}"
