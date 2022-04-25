from django.urls import path,re_path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.UploadListAPI.as_view(),name='upload-list'),
    path('new/',views.UploadFileCreateApi.as_view(),name='upload-file'),
    path('<int:id>/detail',views.UploadFileDetailApi.as_view(),name='file-detail'),
    path('<int:id>/delete',views.UploadFileDeleteApi.as_view(),name='edit-file'),
    path('<int:id>/edit',views.UploadFileUpdateApi.as_view(),name='edit-file'),
]


