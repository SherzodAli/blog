# Generated by Django 3.1 on 2020-08-10 12:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200810_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(db_index=True, verbose_name='Текст'),
        ),
    ]
