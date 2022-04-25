from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.UploadFile)
class UploadFileRegister(admin.ModelAdmin):
    list_display = ('uploadDate',)
