from core.serializers import (
    LivroSerializer,
    FormapagamentoSerializer,
    RegisterUserSerializer,
)
from core.models import Livro, Formapagamento
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import mixins
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class LivroViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["categoria", "titulo", "autor"]
    filterset_fields = ["categoria", "titulo", "autor"]


class FormapagamentoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Formapagamento.objects.all()
    serializer_class = FormapagamentoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]


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
