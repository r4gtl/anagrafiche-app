from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Cliente, Fornitore
from .serializers import ClienteSerializer, FornitoreSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["ragione_sociale", "partita_iva"]
    ordering_fields = ["ragione_sociale", "partita_iva"]

class FornitoreViewSet(viewsets.ModelViewSet):
    queryset = Fornitore.objects.all()
    serializer_class = FornitoreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["ragione_sociale", "partita_iva"]
    ordering_fields = ["ragione_sociale", "partita_iva"]
