from core.serializers import LivroSerializer, FormapagamentoSerializer
from core.models import Livro, Formapagamento
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import mixins


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
