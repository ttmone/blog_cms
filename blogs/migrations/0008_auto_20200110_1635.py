# Generated by Django 3.0.2 on 2020-01-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20200110_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(blank=True, to='blogs.Comment', verbose_name='コメント'),
        ),
    ]
