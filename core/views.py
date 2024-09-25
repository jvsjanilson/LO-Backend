from core.serializers import RegisterUserSerializer
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class UserAuthenticadedViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            "username": user.username,
            "email": user.email,
        }
        return JsonResponse(user_data, safe=False)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)
