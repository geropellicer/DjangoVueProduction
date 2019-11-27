from requests import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import exceptions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet



from canchas.models import Cancha, Alquiler
from canchas.api.serializers import CanchaSerializer, AlquilerSerializer

# class ListaPerfiles(generics.ListAPIView):
#     queryset = Perfil.objects.all()
#     serializer_class = PerfilSerializer
#     permission_classes = [IsAuthenticated]

# class AvatarUpdateView(generics.UpdateAPIView):
#     serializer_class = AvatarPerfilSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         profile_object = self.request.user.perfil
#         return profile_object

class CanchasViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['nombre']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlquileresViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['cancha.nombre']
    

    def perform_create(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

# class EstadoPerfilViewSet(ModelViewSet):
#     serializer_class = EstadoPerfilSerializer
#     permission_classes = [IsAuthenticated, EsOwnerOrReadOnly]

#     def get_queryset(self):
#         queryset = EstadoPerfil.objects.all()
#         username = self.request.query_params.get("username", None)
#         if username is not None:
#             queryset = queryset.filter(perfil_usuario__usuario__username=username)
#         return queryset

#     def perform_create(self, serializer):
#         perfil_usuario = self.request.user.perfil
#         serializer.save(perfil_usuario=perfil_usuario)
