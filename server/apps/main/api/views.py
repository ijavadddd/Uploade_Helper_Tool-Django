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



from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadFileSerializer

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        file_serializer = UploadFileSerializer(data=request.data)
        if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def post(self, request, *args, **kwargs):
        file_serializer = UploadFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)