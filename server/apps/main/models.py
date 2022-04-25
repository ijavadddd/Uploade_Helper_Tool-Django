from django.db import models

# Create your models here.

class UploadFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='documents')
    uploadDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.uploadDate}'