from .models import Servicio

from rest_framework import viewsets, permissions

from .serializers import ServicioSerializer

class ServicioviewSet(viewsets.ModelViewSet):
	queryset = Servicio.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = ServicioSerializer