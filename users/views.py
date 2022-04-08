from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from users.models import ExtendedUser, Status
from .serializers import ExtendedUserSerializer, StatusSerializer, TokenSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExtendedUserSerializer


class ObtainTokenView(ObtainAuthToken):
    def post(self, request):
        serializer = TokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'auth-token': token.key,
        }, status=status.HTTP_200_OK)


class CreateStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        user = ExtendedUser.objects.get(phone_number=request.data["phone_number"])
        serializer = StatusSerializer(data={
            "user": user.id,
            "status": request.data["status"],
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
