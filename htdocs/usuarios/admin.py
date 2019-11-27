from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import Usuario, Amistad, Solicitud


class UsuarioAdmin(UserAdmin):
    # add_form = 
    # form = 
    model = Usuario
    list_display = ["username", "email", "is_staff"]


admin.site.register(Usuario, UsuarioAdmin)
