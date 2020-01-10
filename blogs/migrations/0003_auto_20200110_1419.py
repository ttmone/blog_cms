# Generated by Django 3.0.2 on 2020-01-10 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200110_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='コメントタイトル')),
                ('text', models.TextField(verbose_name='コメント本文')),
                ('username', models.CharField(max_length=140, verbose_name='ニックネーム')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='タグ名')),
                ('description', models.TextField(blank=True, null=True, verbose_name='説明')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無し', max_length=140, verbose_name='ユーザー名')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, verbose_name='公開する'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='未分類', max_length=140, verbose_name='カテゴリ名'),
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blogs.Comment', verbose_name='コメント'),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='blogs.Tag', verbose_name='タグ'),
        ),
    ]
