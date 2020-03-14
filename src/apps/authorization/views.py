import logging
from datetime import datetime
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView

# My libs
from apps.authorization.models import Services
from apps.authorization.usecases import LdapBackend
from apps.authorization.serializers import AuthSerializer, LdapSerializer
from apps.contribe.permissions import UsersPermissions
from apps.contribe.logging_module import Logger


class LdapAuthViewSet(CreateAPIView):
    serializer_class = AuthSerializer
    http_method_names = [u'post']
    permission_classes = (UsersPermissions,)

    # Allow method
    def post(self, request, *args, **kwargs):
        logger = Logger._logging(LdapAuthViewSet.__name__)

        serializer_data = AuthSerializer(request.data).data
        response = LdapBackend.get_ldap_user(username=serializer_data['username'],
                                             password=serializer_data['password'])

        if response:
            service = Services.objects.get(token=request.data.get('token'))
            serializer = LdapSerializer(
                data=response,
                context={'request': request},
                service=service)

            serializer.is_valid()

            logger.warning(f"\nUSER ==> {serializer_data['username']}"
                           f"\nDate ===> {datetime.now()}"
                           f"\nUser(Data) ==> {str(serializer.data)}"
                           f"\nStatus ===> 200_OK\n")
            return Response(serializer.data, status=HTTP_200_OK)

        logger.warning(f"\nUSER==> {serializer_data['username']}"
                       f"\nDate ===> {datetime.now()}"
                       f"\nUser(Data)==> 400_BAD\n")
        return Response(status=HTTP_400_BAD_REQUEST)
