# Generated by Django 3.2.5 on 2022-04-25 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_uploadfile_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='description',
        ),
    ]
