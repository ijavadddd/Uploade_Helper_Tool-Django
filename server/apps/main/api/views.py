from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from apps.main import models
from . import serializers


##List of all uploaded files
class UploadFileListAPI(generics.ListAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileListSerializer


##Upload new file by api page
class UploadFileCreateApi(generics.CreateAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileCreatSerializer


##Detail of uploaded instance by id
class UploadFileDetailApi(generics.RetrieveAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileDetailSerializer
    lookup_field = 'id'


##Delete uploaded instance by id
class UploadFileUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileDetailSerializer
    lookup_field = 'id'


##Delete each uploded file that id entered in urls
class UploadFileDeleteApi(generics.RetrieveDestroyAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileDeleteSerializer
    lookup_field = 'id'


##With this class we can update & delete files in a page
class UploadFileManageApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UploadFile.objects.all()
    serializer_class = serializers.UploadFileManageSerializer
    lookup_field = 'id'


##Upload files with script(CLI.py)
class UploadFileAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = serializers.UploadFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            # print(file_serializer.errors)
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        