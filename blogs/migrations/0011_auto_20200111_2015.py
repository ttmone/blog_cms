# Generated by Django 3.0.2 on 2020-01-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20200110_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blogs', verbose_name='サムネイル'),
        ),
    ]
