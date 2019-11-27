from django.urls import path, include
from rest_framework.routers import DefaultRouter
from canchas.api.views import CanchasViewSet, AlquileresViewSet

router = DefaultRouter()
router.register(r"canchas", CanchasViewSet)
router.register(r"alquileres", AlquileresViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('avatar/', AvatarUpdateView.as_view(), name="avatar-update")
]
