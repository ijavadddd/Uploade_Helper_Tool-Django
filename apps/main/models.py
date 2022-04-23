from django.db import models

# Create your models here.

class Upload(models.Model):
    url = models.CharField(max_length=550)
    upload_date = models.DateField(auto_now_add=True)