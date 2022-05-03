from django.db import models

# Create your models here.

# Model of uploader
class UploadFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='documents', null=True)
    uploadDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.file} {self.uploadDate}'


