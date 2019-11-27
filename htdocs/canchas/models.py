from django.db import models

# Create your models here.

class Cancha(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20, unique=True)
    TIPOS_CANCHA = (
                        ('Cancha de 11','11'),
                        ('7ABIERTA', 'Cancha de 7 abierta'),
                        ('5ABIERTA', 'Cancha de 5 abierta'),
                        ('7TECHADA', 'Cancha de 7 techada'),
                        ('5TECHADA', 'Cancha de 5 techada')
                    )
    tipo = models.CharField(max_length=20, choices=TIPOS_CANCHA, default='Cancha de 5 techada')
    tiene_vestuario = models.BooleanField(default=False)
    tiene_iluminacion = models.BooleanField(default=False)
    tiene_cesped_sintetico = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "canchas"

class Alquiler(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name="alquileres")
    cliente = models.CharField(max_length=50)
    empleado = models.CharField(max_length=50)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    turno_desde = models.DateTimeField()
    turno_hasta = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = "alquileres"
