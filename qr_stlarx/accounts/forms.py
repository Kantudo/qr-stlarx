from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class SignUpForm(UserCreationForm, forms.Form):
    #username = forms.CharField(max_length=30)
    #email = forms.EmailField(max_length=200)

    username = forms.CharField(widget=TextInput(attrs={'type': 'text',
                                                       'name': 'username',
                                                       'id': 'username',
                                                       'autocomplete': 'off',
                                                       'class': 'validate'}))
    email = forms.CharField(widget=TextInput(attrs={'type': 'text',
                                                       'name': 'email',
                                                       'id': 'email',
                                                       'autocomplete': 'off',
                                                       'class': 'validate'}))
    password1 = forms.CharField(widget=TextInput(attrs={'type': 'password',
                                                       'name': 'password1',
                                                       'id': 'password1',
                                                       'autocomplete': 'off',
                                                       'class': 'validate'}))
    password2 = forms.CharField(widget=TextInput(attrs={'type': 'password',
                                                       'name': 'password2',
                                                       'id': 'password2',
                                                       'autocomplete': 'off',
                                                       'class': 'validate'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class AuthForm(PopRequestMixin, CreateUpdateAjaxMixin, AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'type': 'text',
                                                       'name': 'username',
                                                       'id': 'username',
                                                       'autocomplete': 'off',
                                                       'class': 'validate'}))
    password = forms.CharField(widget=TextInput(attrs={'type': 'password',
                                                       'name': 'password',
                                                       'id': 'password',
                                                       'autocomplete': 'off',
                                                       'class': 'validate'}))
