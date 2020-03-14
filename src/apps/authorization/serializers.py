from rest_framework import serializers

# My Libs
from apps.contribe.serializers import BaseSerializer
from apps.authorization.models import SettingField


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField()


class LdapSerializer(BaseSerializer):

    def __init__(self, *args, **kwargs):

        # Response from LDAP
        data = kwargs.get('data')
        attributes = data.get('attributes')

        # Take full name from ldap fields
        name_data = attributes.get('givenName')

        name = None
        middle_name = None

        if name_data:
            name_data = name_data.split()

            name = name_data[0]
            middle_name = ""

            if len(name_data) >= 2:
                middle_name = name_data[1]

        name = self.validation_fields(name)
        middle_name = self.validation_fields(middle_name)
        last_name = self.validation_fields(attributes.get('sn'))

        # new data field / Default value
        new_data = {
            'raw_dn_info': data['raw_dn_info'].decode(),
            'givenName': name,
            'givenMiddleName': middle_name,
            'sAMAccount': attributes.get('sAMAccount'),
            'mail': attributes.get('mail'),
            'sn': last_name,
            'title': attributes.get('title'),
            'telephoneNumber': attributes.get('telephoneNumber'),
        }

        service = kwargs.pop('service')
        # Get other field from settings
        setting_field = SettingField.objects.filter(service=service)

        for key_field in setting_field:
            value_ldap = attributes.get(key_field.field_ldap)
            if value_ldap:
                new_data[key_field.field_ldap] = value_ldap

        for key in new_data:
            self.fields[key] = serializers.CharField()

        kwargs['data'] = new_data

        super(LdapSerializer, self).__init__(*args, **kwargs)

    def validation_fields(self, obj_field):
        if obj_field:
            return obj_field
        return "LDAP DOESNOT HAVE FIELD"
