# Generated by Django 2.1.4 on 2018-12-10 19:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20181210_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='monitoring_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]