from django import forms
from . import models

class UploadForm(forms.ModelForm):

    class Meta:
        model = models.UploadFile
        fields = '__all__'
        widgets = {
            'file':forms.FileInput(attrs={'id':'upload-fiels','class':'my-2'}),
        }







