from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from middleware.security import AllowAny
from django.shortcuts import render
from entities import models
from django.db.models import F, Q, Sum
from .serializers import *
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
import bcrypt


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        # Validate user access
        user = models.User.objects.filter(username=username).first()

        if not user:
            return Response("Invalid username or password",
                            status=status.HTTP_401_UNAUTHORIZED,)

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode()):
            return Response("Invalid username or password",
                            status=status.HTTP_401_UNAUTHORIZED,)

        new_token = get_random_string(length=32)
        expires = datetime.now() + timedelta(hours=1)

        usersession = models.UserSession.objects.filter(user_id=user.id).first()
        if usersession:
            usersession.delete()
        models.UserSession(user=user,
                            token=new_token,
                            expires=expires).save()
        return Response({
            'token': new_token
        })


class CurrentUserContext(APIView):
    
    def get(self, request, token=None, *args, **kwargs):
        serializer = CurrentUserContextSerializer
        serializer = serializer(request.user)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)


class Logout(APIView):
    def post(self, request, *args, **kwargs):
        return
        # existingUser = self.request.user
        # if existingUser:
        #     existingToken = Token.objects.filter(user=existingUser).first()
        #     if existingToken:
        #         existingToken.delete()
        #         return Response(data={"detail": "User was logged out"},
        #                         status=status.HTTP_200_OK)
        #     else:
        #         return Response(data={"detail": "User session not found"},
        #                         status=status.HTTP_404_NOT_FOUND)
        # else:
        #     return Response(data={"detail": "User not found"},
        #                     status=status.HTTP_404_NOT_FOUND)


class RefreshToken(APIView):
    def post(self, request, token=None, *args, **kwargs):
        return
        # existingToken = Token.objects.filter(key=token).first()
        # if existingToken:
        #     if existingToken.user == request.user:
        #         existingToken.created = datetime.now()
        #         existingToken.save()
        #         return Response(data={"detail": "Token refreshed"},
        #                         status=status.HTTP_200_OK)
        #     else:
        #         return Response(data={"detail": "Token user not match"},
        #                         status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     return Response(data={"detail": "Token not found"},
        #                     status=status.HTTP_404_NOT_FOUND)


'''
***********************
** RESET CREDENTIALS **
***********************
'''


class ForgotPassword(APIView):

    def post(self, request, username=None, *args, **kwargs):
        return
        # existingUser = User.objects.filter(username=username).first()

        # if existingUser:
        #     # Check if there's existing request
        #     exToken = AuthToken\
        #               .objects\
        #               .filter(
        #                   user_id=existingUser.id,
        #                   is_active=True)\
        #               .first()
        #     if exToken:
        #         raise Exception(
        #             'There is an existing password reset for this user.')

        #     REF = 'AUTH'
        #     TOKEN = ''
        #     TIMEOUT = 10000
        #     PASSCODE = 0

        #     # Generate Random token for TOKEN
        #     TOKEN = Token().generate_key()

        #     # Generate Random number for PASSCODE
        #     rands = []
        #     rands.append(randrange(10))
        #     rands.append(randrange(10))
        #     rands.append(randrange(10))
        #     rands.append(randrange(10))
        #     PASSCODE = f"{rands[0]}{rands[1]}{rands[2]}{rands[3]}"

        #     AuthToken(
        #         ref=REF,
        #         token=TOKEN,
        #         passcode=PASSCODE,
        #         timeout=TIMEOUT,
        #         is_active=True,
        #         user=existingUser,
        #     ).save()

        #     url = f"{settings.FRONT_END_URL}/account/forgot-password-reset"\
        #           f"?token={TOKEN}"

        #     sender.forgot_password(
        #         str(PASSCODE),
        #         str(url),
        #         str(existingUser.email))

        #     return Response(data={"detail": "Forgot Password Sent"},
        #                     status=status.HTTP_200_OK)
        # else:
        #     return Response(data={"error": "User not found"},
        #                     status=status.HTTP_404_NOT_FOUND)


class ValidateForgotPasswordResetToken(APIView):

    def post(self, request, token=None, *args, **kwargs):
        return 
        # existingToken = AuthToken.objects.filter(token=token).first()
        # if existingToken:
        #     if not existingToken.is_active:
        #         raise Exception('Request is no longer active')
        #     return Response(data={
        #                         "username": existingToken.user.username,
        #                         "email": existingToken.user.email
        #                     },
        #                     status=status.HTTP_200_OK)
        # else:
        #     return Response(data={"error": "Token not found"},
        #                     status=status.HTTP_404_NOT_FOUND)


class ForgotPasswordReset(APIView):

    def post(self, request, token=None, *args, **kwargs):
        return
        # body_unicode = request.body.decode('utf-8')
        # body_data = json.loads(body_unicode)

        # username = body_data['username']
        # password = body_data['password']
        # password_confirm = body_data['password_confirm']
        # passcode = body_data['passcode']

        # if not username:
        #     raise Exception('Username is required')

        # if not passcode:
        #     raise Exception('Passcode is required')

        # if password != password_confirm:
        #     raise Exception('Passwords must match')

        # existingToken = AuthToken.objects.filter(token=token).first()

        # if existingToken:

        #     if existingToken.user.username != username:
        #         raise Exception('Username does not match')

        #     if not existingToken.is_active:
        #         raise Exception('Request is no longer active')

        #     if existingToken.passcode != passcode:
        #         raise Exception('Invalid Passcode')

        #     # TODO: Reset password here
        #     exUser = User.objects.filter(id=existingToken.user.id).first()
        #     exUser.set_password(password_confirm)
        #     exUser.save()

        #     existingToken.is_active = False
        #     existingToken.save()

        #     sender.password_changed(
        #         str(existingToken.user.username),
        #         str(datetime.now()),
        #         str(existingToken.user.email))

        #     return Response(data={"detail": "Forgot Password Reset Success"},
        #                     status=status.HTTP_200_OK)
        # else:
        #     return Response(data={"error": "Token not found"},
        #                     status=status.HTTP_404_NOT_FOUND)
