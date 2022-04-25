from django import forms
from . import models

class Upload(forms.ModelForm):

    class Meta:
        model = models.UploadFile
        fields = '__all__'
        widgets = {
            'file':forms.FileInput(attrs={'id':'upload-fiels','class':'my-2','multiple': 'True'}),
        }







