from django.contrib import admin

# My models
from apps.authorization.models import LdapSettings, Services, SettingField


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'token'
    ]


@admin.register(LdapSettings)
class NotificationsMessengersAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'settings',
    ]


@admin.register(SettingField)
class NotificationsMessengersAdmin(admin.ModelAdmin):
    fields = [
        'service',
        'field_ldap',
        'description'
    ]
