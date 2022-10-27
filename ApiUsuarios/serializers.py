from rest_framework import serializers

from .models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = ('referencia','nombre','descripcion','nuevo','precio')
		read_only_fields = ('fecha',)