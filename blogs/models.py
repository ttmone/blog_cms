from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=140, verbose_name='カテゴリ名', default='未分類')
    description = models.TextField(blank=True, null=True, verbose_name='説明')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=140, verbose_name='タグ名')
    description = models.TextField(blank=True, null=True, verbose_name='説明')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=140, verbose_name='ユーザー名', default='名無し')

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=140, verbose_name='コメントタイトル')
    text = models.TextField(verbose_name='コメント本文')
    username = models.CharField(max_length=140, verbose_name='ニックネーム')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=140, verbose_name='タイトル')
    text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    published_at = models.DateTimeField(verbose_name='投稿日時')
    updated_at = models.DateTimeField(verbose_name='更新日時')
    category = models.ManyToManyField(Category, verbose_name='カテゴリ')
    tag = models.ManyToManyField(Tag, verbose_name='タグ', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='執筆者', on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, verbose_name='コメント', on_delete=models.PROTECT, null=True, blank=True)
    published = models.BooleanField(verbose_name='公開する', default=False)

    def __str__(self):
        return self.title
