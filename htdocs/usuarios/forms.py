from django_registration.forms import RegistrationForm
from usuarios.models import Usuario


class UsuarioForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = Usuario
