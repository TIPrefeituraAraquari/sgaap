# -*- coding: utf-8 -*-
# from django.core.urlresolvers import reverse
# from usuarioapp.models.instituicao import Instituicao
# from usuarioapp.models.email import Email
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse



class ComplementoUsuario(models.Model):
    '''
    :param user_id: models.ForeignKey(User, related_name="user", verbose_name="ID do Usuário (Auth User)", help_text='Deve conter o usuário.')
    :param lista_email: models.ManyToManyField(Email, verbose_name="E-mails", help_text='Deve conter os e-mails relacionados ao usuário.')
    :param instituicao: models.ManyToManyField(Instituicao, verbose_name="Instituição", help_text='Deve conter as Instuições, Universidades ou Organizações.')
    :param nome: models.CharField(max_length=500)
    '''
    user = models.OneToOneField(User, related_name='user_user', verbose_name='ID do Usuário (Auth User)',
                                   help_text='Deve conter o usuário.',on_delete=SET_NULL, null=True)
    imagem = models.ImageField(upload_to='usuario/imagem', null=True)
    excluido = models.BooleanField(default=False, verbose_name="Excluído")
    desativado = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('complento-usuario-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = 'usuarioapp'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = (
            ("list_complento_usuario", "Can list"),
            ("detail_complemento_usuario", "Can detail"),
            ("list_convidado", "Can list convidado"),
            ("detail_convidado", "Can detail convidado"),
            ("change_convidado", "Can change convidado"),
            ("add_convidado", "Can add convidado"),
            ("delete_convidado", "Can delete convidado"),
            ("list_user", "Can list convidado"),
            ("detail_user", "Can detail convidado"),
        )
