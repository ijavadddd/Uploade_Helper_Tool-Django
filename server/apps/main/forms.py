from django import forms
from . import models

# Form model of UploadFile model for use in UI Uploader
class UploadForm(forms.ModelForm):

    class Meta:
        model = models.UploadFile
        fields = '__all__'
        widgets = {
            'file':forms.FileInput(attrs={'id':'upload-fiels','class':'my-2'}),
        }







