from django import forms
from django.core.validators import FileExtensionValidator
from .validators import FileSizeValidator
from django.forms.widgets import TextInput

class str2qr_charfield(forms.Form):
    str2encode = forms.CharField(widget=TextInput(attrs={'type': 'text',
                                                       'name': 'str2encode',
                                                       'id': 'str2encode',
                                                       'autocomplete': 'off'}))

class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf']), FileSizeValidator(allowed_size=50)])
