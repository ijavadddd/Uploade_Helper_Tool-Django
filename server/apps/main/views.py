from django.shortcuts import render
from django.views import View
from . import forms
# Create your views here.

##This class will render Home page
class Index(View):

    def get(self, request):
        context={'upload_form':forms.Upload}
        return render(request, 'main/index.html',context)

    def post(self, request):
        context={'upload_form':forms.Upload}
        form = forms.Upload(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file = file.chunks(chunk_size=None)
            file_name = file.name
            print(file_name)
        return render(request, 'main/index.html',context)
        
