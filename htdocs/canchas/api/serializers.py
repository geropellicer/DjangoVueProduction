from rest_framework import serializers
from canchas.models import Cancha, Alquiler


class AlquilerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alquiler
        fields = "__all__"


class CanchaSerializer(serializers.ModelSerializer):
    alquileres = AlquilerSerializer(many=True)

    class Meta:
        model = Cancha
        fields = "__all__"


