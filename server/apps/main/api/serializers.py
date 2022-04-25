from rest_framework.serializers import ModelSerializer
from apps.main import models


class UploadFileListSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'


class UploadFileCreatSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'


class UploadFileDetailSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'
        lookup_field = 'id'


class UploadFileDeleteSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'
        lookup_field = 'id'


class UploadFileUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'
        lookup_field = 'id'


class UploadFileSerializer(ModelSerializer):
    class Meta:
        model = models.UploadFile
        fields = '__all__'