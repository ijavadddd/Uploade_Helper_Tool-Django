from django.urls import path,re_path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.UploadFileListAPI.as_view(),name='upload-list'),
    path('create-new/',views.UploadFileCreateApi.as_view(),name='upload-file'),
    path('new/',views.UploadFileAPI.as_view(),name='upload-file'),
    path('<int:id>/detail',views.UploadFileDetailApi.as_view(),name='file-detail'),
    path('<int:id>/edit',views.UploadFileUpdateApi.as_view(),name='edit-file'),
    path('<int:id>/delete',views.UploadFileDeleteApi.as_view(),name='delete-file'),
    path('<int:id>/manage',views.UploadFileManageApi.as_view(),name='manage-file'),
]


