# coding=utf-8
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import *
from usuarioapp.forms.validation.email import *


class UserForm(ModelForm):
    first_name = forms.CharField(required=True, label='Primeiro Nome',
                                 widget=forms.TextInput(attrs={'placeholder': 'Primeiro Nome',
                                                               'class': 'form-control'}))
    last_name = forms.CharField(required=True, label='Último Nome',
                                widget=forms.TextInput(attrs={'placeholder': 'Sobrenome',
                                                              'class': 'form-control'
                                                              }))
    email = forms.EmailField(required=True, label='Email',
                             widget=forms.EmailInput(attrs={'placeholder': 'exemplo@exemplo.com',
                                                            'class': 'form-control'
                                                            }))
    password = forms.CharField(required=True, label='Senha', widget=forms.PasswordInput(
                                                            attrs={'placeholder': '******',
                                                            'class': 'form-control'
                                                            }))
    password_checker = forms.CharField(required=True, label='Confirmar Senha', widget=forms.PasswordInput(
                                                            attrs={'placeholder': '******',
                                                            'class': 'form-control'
                                                            }))

    def clean_password_checker(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password_checker = self.cleaned_data['password_checker']
            if password == password_checker:
                return password_checker
            else:
                raise forms.ValidationError('As senhas são diferentes!')
        else:
            raise forms.ValidationError('As senhas são diferentes!')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    def clean_email(self):

        return ValidationEmail(self.cleaned_data.get("email"))


class UserEditForm(ModelForm):
    password = ReadOnlyPasswordHashField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Nova Senha', 'value': u'Império Contra Ataca'}), label='Nova Senha')
    password_checker = forms.CharField(required=True,
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Senha'}),
                                       label='Confirmar Senha')

    def clean_password_checker(self):

        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password_checker = self.cleaned_data['password_checker']
            if password == password_checker:
                return password_checker
            else:
                raise forms.ValidationError('As senhas são diferentes!')
        else:
            raise forms.ValidationError('As senhas são diferentes!')

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'is_active')


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class CreateEmailForm(ModelForm):
    def clean_email(self):
        return ValidationEmail(self.cleaned_data.get("email"))

    class Meta:
        model = User
        fields = ('email',)


class UserConvidadoForm(ModelForm):
    first_name = forms.CharField(required=True, label='Primeiro Nome',
                                 widget=forms.TextInput(attrs={'placeholder': 'Primeiro Nome'}))
    last_name = forms.CharField(required=True, label='Último Nome',
                                widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'}))
    email = forms.EmailField(required=True, label='E-mail', help_text='O e-mail deve ser único.',
                             widget=forms.EmailInput(attrs={'placeholder': 'exemplo@exemplo.com'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def clean_email(self):
        return ValidationEmailConvidado(self.cleaned_data.get("email"))
