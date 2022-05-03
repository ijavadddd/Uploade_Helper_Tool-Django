from posixpath import split
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from . import forms
from . import models
from django.conf import settings
from django.urls import reverse

# This class will render Home page(UI Uploader)
class Index(View):

    def get(self, request):
        context={'upload_form': forms.UploadForm, 'media':settings.MEDIA_URL}
        return render(request, 'main/index.html',context)

    def post(self, request):
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save uploaded file to db as object
            newFile = models.UploadFile(file=request.FILES['file'])
            newFile.save()
            uploadedFileDetail = list(str(newFile).split())

        # else:  # It' for debug
            # print(form.errors)
        context={'uploaded_file_detail': {'id':uploadedFileDetail[0], 'url':uploadedFileDetail[1], 'dateOfPublish':uploadedFileDetail[2]}, 'media':settings.MEDIA_URL}
        # successfullyUpload = reverse('success_upload')
        return render(request,'main/success_upload.html',context)



