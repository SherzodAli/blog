# Generated by Django 3.1 on 2020-08-10 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Ссылка')),
                ('summary', models.TextField(blank=True, db_index=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
        ),
    ]