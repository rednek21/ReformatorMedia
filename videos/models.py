from django.db import models


# Create your models here.

class Theme(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        db_table = "theme"
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        # ordering =

    def __str__(self):
        return f'{self.title}'


class Video(models.Model):
    title = models.CharField(max_length=128)
    theme = models.ForeignKey(to=Theme, on_delete=models.SET_NULL, null=True)
    url = models.URLField()

    class Meta:
        db_table = "video"
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        # ordering =

    def __str__(self):
        return f'{self.title}'
