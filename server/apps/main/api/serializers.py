from rest_framework.serializers import ModelSerializer
from apps.main import models


##All Uploaded file list serializer
class UploadFileListSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'


##Upload new file serializer
class UploadFileCreatSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'


##Uploaded file detail by id serializer
class UploadFileDetailSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'
        lookup_field = 'id'


##Update an instance of files serializer
class UploadFileUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'
        lookup_field = 'id'


##Delete instances by id serializer
class UploadFileDeleteSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'
        lookup_field = 'id'


##Delete or update (manage) instances by id serializer
class UploadFileManageSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'
        lookup_field = 'id'


##Upload files by Cli.py serializer
class UploadFileSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = "__all__"