from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    """
    BaseSerializer allow restrict fields that don't use.
    Example:
        Base model:
            {
                "name": "",
                "date": "",
                "date_created": ""
            }
        when use fields parameter you can filter fields:

        /api/bases?fields=name,date
        returns:
            {
                "name": "Base",
                "date": "2019/12/28 23:59:59"
            }

    """
    def __init__(self, *args, **kwargs):

        super(BaseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")

        if request and request.query_params.get('fields'):
            fields = request.query_params.get('fields')

            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())

                for field_name in existing - allowed:
                    self.fields.pop(field_name)




