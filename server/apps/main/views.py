from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from . import forms
from . import models
from django.conf import settings
from django.urls import reverse
import os


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
            uploadedFileDetail = (str(newFile).split())

        # else:  # It' for debug
            # print(form.errors)
        context={'uploaded_file_detail': {'id':uploadedFileDetail[0], 'url':uploadedFileDetail[1], 'dateOfPublish':uploadedFileDetail[2]}, 'media':settings.MEDIA_URL}
        return redirect('upload-file',uploadedFileDetail[0])


class SuccessUpload(View):
    def get(self, request, fileId):
        file = models.UploadFile.objects.filter(id=fileId)
        fileDetail = str(file[0]).split()
        context={
        'uploaded_file_detail': {'id':fileDetail[0], 
        'url':fileDetail[1], 
        'dateOfPublish':fileDetail[2]}, 
        'media':settings.MEDIA_URL
        }
        return render(request,'main/success_upload.html',context)


class DeleteFile(View):
    def get(self, request, fileId):
        file = models.UploadFile.objects.filter(id=fileId)
        fileAddress = str(file[0]).split()
        fileAddress = fileAddress[1]
        FILES_DIR = os.path.join(settings.MEDIA_ROOT,fileAddress)
        os.remove(FILES_DIR)
        file.delete()
        return render(request, 'main/delete_file.html')
        

