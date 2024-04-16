# Generated by Django 5.0.4 on 2024-04-16 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0001_initial'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.RemoveField(
            model_name='video',
            name='themes',
        ),
        migrations.AddField(
            model_name='video',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='themes.theme'),
        ),
    ]