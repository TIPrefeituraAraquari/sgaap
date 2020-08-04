from django.forms import *
from usuarioapp.models.instituicao import Instituicao


class InstituicaoForm(ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'
