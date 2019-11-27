from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    pass

class Amistad(models.Model):
    amigoPropone = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ami1")
    amigoPropuesto = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ami2")

    class Meta:
        verbose_name_plural = "amistades"
    
    def __str__(self):
        return 'Amistad de '+ self.amigoPropone.username+ " y "+ self.amigoPropuesto.username

class Solicitud(models.Model):
    solicitado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="sol1")
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="sol2")
    confirmada = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "solicitudes"
    
    def __str__(self):
        return 'Solicituf de '+ self.solicitante.username+ " a "+ self.solicitado.username
