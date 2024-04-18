from django.db import models


class Theme(models.Model):
    title = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = "theme"
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        # ordering =

    def __str__(self):
        return f'{self.title}'
