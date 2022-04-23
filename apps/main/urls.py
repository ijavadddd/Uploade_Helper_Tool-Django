from django.urls import path
#Import views for call view classes and functions
from . import views

urlpatterns={
    path('',views.Index.as_view(),name='home')
}

