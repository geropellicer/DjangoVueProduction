from django.urls import path
from usuarios.api.views import CurrentUserAPIView

urlpatterns = [
    path("m/perfiles/usuario/", CurrentUserAPIView.as_view(), name="current-user")
]