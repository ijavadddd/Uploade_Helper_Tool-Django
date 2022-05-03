from cgitb import html
from django.urls import path
#Import views for call view classes and functions
from . import views
from django.views.generic.base import RedirectView

urlpatterns= [
    path('',views.Index.as_view(),name='home'),
    path('<int:fileId>/uploaded',views.SuccessUpload.as_view(), name='upload-file'),
    path('<int:fileId>/delete',views.DeleteFile.as_view(), name='delete-file'),
]

