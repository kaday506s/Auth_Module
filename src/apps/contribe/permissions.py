from rest_framework import permissions

# My libs
from apps.authorization.models import Services


class UsersPermissions(permissions.BasePermission):
    """
        Method for checking permissions to user
    """

    def has_permission(self, request, view, *args, **kwargs):

        try:
            Services.objects.get(token=request.data.get('token'))

            return True
        except Services.DoesNotExist:
            return False
