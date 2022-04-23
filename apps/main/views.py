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
        form = forms.Upload(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            file_name = data['file']
            print(file_name)
        return render(request, 'main/index.html')
        
