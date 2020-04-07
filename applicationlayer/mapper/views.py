from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from middleware.security import AllowAny
from django.shortcuts import render
from entities import models
from django.db.models import F, Q, Sum
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from applicationlayer import utils
from django.conf import settings
import bcrypt
import copy
import requests
# from requests import Request, Session


class EntryPoint(APIView):
    http_method_names = ['get',
                         'post',
                         'put',
                         'patch',
                         'delete']

    def get_request_headers(self, request):
        token = None
        auth = request.headers.get("Authorization")
        if auth:
            token = auth.replace('Bearer ', '')

        if token:
            return {"Authorization": 'Bearer ' + token}
        else:
            return {}

    def return_request(self, response):
        response_body = None
        try:
            response_body = response.json()
        except:
            pass
        return Response(response_body,
                        status=response.status_code)

    def get(self, request, *args, **kwargs):
        values = utils.get_request_values(request)
        return self.return_request(
            requests.get(
                url=values.get('target_destination'),
                headers=self.get_request_headers(request)
            )
        )

    def post(self, request, *args, **kwargs):
        values = utils.get_request_values(request)
        return self.return_request(
            requests.post(
                url=values.get('target_destination'),
                data=values.get('client_body'),
                headers=self.get_request_headers(request)
            )
        )

    def put(self, request, *args, **kwargs):
        values = utils.get_request_values(request)
        return self.return_request(
            requests.put(
                url=values.get('target_destination'),
                data=values.get('client_body'),
                headers=self.get_request_headers(request)
            )
        )

    def patch(self, request, *args, **kwargs):
        values = utils.get_request_values(request)
        return self.return_request(
            requests.patch(
                url=values.get('target_destination'),
                data=values.get('client_body'),
                headers=self.get_request_headers(request)
            )
        )

    def delete(self, request, *args, **kwargs):
        values = utils.get_request_values(request)
        return self.return_request(
            requests.delete(
                url=values.get('target_destination'),
                headers=self.get_request_headers(request)
            )
        )

