# Generated by Django 3.2.5 on 2022-04-23 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_upload_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='s',
        ),
    ]
