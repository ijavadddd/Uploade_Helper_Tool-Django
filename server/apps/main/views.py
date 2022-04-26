from django.shortcuts import render
from django.views import View
from . import forms
from . import models
from django.core.files.storage import FileSystemStorage
# Create your views here.

##This class will render Home page
class Index(View):

    def get(self, request):
        context={'upload_form': forms.UploadForm}
        return render(request, 'main/index.html',context)

    def post(self, request):
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            upload = models.UploadFile(file=request.FILES['file'])
            upload.save()

        else:
            print(form.errors)
        context={'upload_form': forms.UploadForm}
        return render(request, 'main/index.html',context)
        