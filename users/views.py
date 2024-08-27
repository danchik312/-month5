from rest_framework import status, views
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import serializers
from .models import ConfirmationCode

class RegisterAPIView(views.APIView):
    def post(self, request):
        serializer = serializers.UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password)
        user.is_active = False
        user.save()

        code = ConfirmationCode.generate_code()
        ConfirmationCode.objects.create(user=user, code=code)

        return Response(data={'user_id': user.id, 'message': 'Please confirm your account'}, status=status.HTTP_201_CREATED)

class ConfirmUserView(views.APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        code = request.data.get('code')

        try:
            confirmation = ConfirmationCode.objects.get(user_id=user_id, code=code)
        except ConfirmationCode.DoesNotExist:
            return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)

        user = confirmation.user
        user.is_active = True
        user.save()

        confirmation.delete()

        token = Token.objects.get_or_create(user=user)[0]

        return Response({'message': 'User confirmed successfully', 'token': token.key}, status=status.HTTP_200_OK)

class LoginAPIView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({'error': 'User is not confirmed'}, status=status.HTTP_400_BAD_REQUEST)

        token = Token.objects.get_or_create(user=user)[0]

        return Response({'token': token.key}, status=status.HTTP_200_OK)