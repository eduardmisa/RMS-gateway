from middleware.current_user.data import set_current_user
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from rest_framework import permissions
from datetime import datetime, timedelta
from django.conf import settings
from entities import models
from applicationlayer import utils
from django.conf import settings
import requests


# class GatewayContextAuthentication(TokenAuthentication):
#     keyword = 'Bearer'

#     def authenticate_credentials(self, key):

#         user_context = None

#         # FETCH current user's context
#         response = requests.get(settings.SERVICE_CONTEXT_HOST + '/api/v1/auth/current-user-context/', headers={"Authorization": self.keyword + ' ' + key})

#         if response.status_code == 200:
#             user_context = response.json()
#         else:
#             message = response.json()
#             if 'detail' in message:
#                 message = message['detail']

#             raise exceptions.AuthenticationFailed(message)

#         return (user_context, key)


class IsAuthenticated(permissions.BasePermission):        

    def has_permission(self, request, view):

        user_context = None

        auth = request.headers.get("Authorization")

        if auth:

            key = auth.replace('Bearer ', '')

            # FETCH current user's context
            response = requests.get(settings.SERVICE_CONTEXT_HOST + '/api/v1/auth/current-user-context/', headers={"Authorization": 'Bearer ' + key})
            if response.status_code == 200:
                user_context = response.json()
            else:
                message = response.json()
                if 'detail' in message:
                    message = message['detail']
                raise exceptions.AuthenticationFailed(message)


        if not user_context:
            return False

        if user_context['is_administrator']:
            return True

        inputs = utils.get_request_inputs(request)
        user = user_context

        permissions = user['application']['permissions'] + user['application']['external_permissions']

        return len(
            list(filter(lambda item: item['url'] == inputs.get('client_path') and item['method'] == inputs.get('client_method'),
                        permissions))
        ) > 0


class AllowAny(permissions.BasePermission):        

    def has_permission(self, request, view):
        return True
