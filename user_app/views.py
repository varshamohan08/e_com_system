from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from django.contrib.auth.models import User
from global_functions import generate_exception


class userLogin(APIView):
    def post(self, request):
        # import pdb;pdb.set_trace()
        try:
            with transaction.atomic():
                username = request.data.get('username', None)
                password = request.data.get('password', None)
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)
                    user_details = {
                        'email': user.email,
                        'username': user.username,
                        'access_token': access_token
                    }

                    return Response({'success':True, 'details': user_details}, status=status.HTTP_200_OK)
                return Response({'success':False, 'details': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            generate_exception(e)
            return Response({'success':False, 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class userLogout(APIView):
    def get(self, request):
        logout(request)
        return Response({'success':True, 'details': 'Logged out successfully'}, status=status.HTTP_200_OK)
