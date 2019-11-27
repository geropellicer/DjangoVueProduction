from rest_framework import serializers
from usuarios.models import Usuario, Amistad, Solicitud

class AmistadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amistad
        fields = "__all__"

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = "__all__"

class UserDisplaySerializer(serializers.ModelSerializer):
    ami1 = AmistadSerializer(many=True)
    ami2 = AmistadSerializer(many=True)
    sol1 = SolicitudSerializer(many=True)
    sol2 = SolicitudSerializer(many=True)

    class Meta:
        model = Usuario
        exclude = ('password',)