from rest_framework import generics
from apps.main import models
from . import serializers

class UploadListAPI(generics.ListAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileListSerializer


class UploadFileCreateApi(generics.CreateAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileCreatSerializer


class UploadFileDetailApi(generics.RetrieveAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileDetailSerializer
    lookup_field = 'id'


class UploadFileDeleteApi(generics.DestroyAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileDeleteSerializer
    lookup_field = 'id'


class UploadFileUpdateApi(generics.UpdateAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileDetailSerializer
    lookup_field = 'id'



