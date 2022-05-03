from cgitb import html
from django.urls import path
#Import views for call view classes and functions
from . import views
from django.views.generic.base import RedirectView

urlpatterns= [
    path('',views.Index.as_view(),name='home'),
]

