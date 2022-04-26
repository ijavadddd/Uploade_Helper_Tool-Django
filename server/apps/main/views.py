from django.shortcuts import render
from django.views import View
from . import forms
from . import models
from django.conf import settings

# This class will render Home page(UI Uploader)
class Index(View):

    def get(self, request):
        context={'upload_form': forms.UploadForm, 'media':settings.MEDIA_URL}
        return render(request, 'main/index.html',context)

    def post(self, request):
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save uploaded file to db as object
            models.UploadFile(file=request.FILES['file']).save()

        # else:
            # print(form.errors)
        context={'upload_form': forms.UploadForm}
        return render(request, 'main/index.html',context)
        