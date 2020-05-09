from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from rest_framework import permissions
from datetime import datetime, timedelta
from django.conf import settings
from applicationlayer import utils
from django.conf import settings
import requests
import re


class IsAuthenticated(permissions.BasePermission):  

    def url_regex_exact_matched (self, regex, string):
        reg = '^' + regex + '$'
        return True if re.match(reg, string) != None else False

    def has_permission(self, request, view):

        user_context = None

        inputs = utils.get_request_values(request)

        # Is Login
        rms_context_allowed_urls = set(['/api/v1/auth/login/', 
                                        '/api/v1/auth/current-user-context/'])

        if inputs['client_path'] in rms_context_allowed_urls:
            return True

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

        if user_context['is_superuser']:
            return True

        permissions = user_context['application']['api_urls']

        return len(
            list(filter(lambda item: self.url_regex_exact_matched(item['url'], inputs.get('client_path'))
                                 and item['method'] == inputs.get('client_method'),
                        permissions))
        ) > 0


class AllowAny(permissions.BasePermission):        

    def has_permission(self, request, view):
        return True
