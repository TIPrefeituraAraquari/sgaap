from django.forms import *
from usuarioapp.models.complemento_usuario import ComplementoUsuario


class UsuarioForm(ModelForm):

    class Meta:
        model = ComplementoUsuario
        exclude = ('user_id', 'username')
