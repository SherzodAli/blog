from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

from apps.utils.slug import _get_unique_slug


class Post(models.Model):
    """Модель поста."""

    title = models.CharField('Заголовок', max_length=255)
    slug = models.CharField('Ссылка', max_length=150, unique=True)
    summary = RichTextUploadingField('Текст', blank=False, db_index=True)
    image = models.ImageField('Картинка', blank=False)
    date = models.DateTimeField('Дата', default=timezone.now)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Картинка'
    admin_photo.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = _get_unique_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
