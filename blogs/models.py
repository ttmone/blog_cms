from django.db import models
from markdownx.models import MarkdownxField


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='カテゴリ名', default='未分類')
    description = models.TextField(blank=True, null=True, verbose_name='説明')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='タグ名')
    description = models.TextField(blank=True, null=True, verbose_name='説明')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='ユーザー名', default='名無し')

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255, verbose_name='ファイル名')
    image_path = models.ImageField(upload_to='blogs', verbose_name='画像')
    image_type = models.CharField(max_length=255, verbose_name='画像タイプ', default='アイキャッチ')

    def __str__(self):
        return self.name


class PostStatus(models.Model):
    name = models.CharField(max_length=255, verbose_name='記事ステータス', default='draft')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='タイトル')
    text = MarkdownxField(verbose_name='本文', help_text='Markdown形式で書いてください。')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(verbose_name='更新日時')
    category = models.ManyToManyField(Category, verbose_name='カテゴリ')
    tag = models.ManyToManyField(Tag, verbose_name='タグ')
    user = models.ForeignKey(User, verbose_name='執筆者', on_delete=models.PROTECT)
    status = models.ForeignKey(PostStatus, verbose_name='ステータス', on_delete=models.PROTECT, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='blogs', verbose_name='サムネイル', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=255, verbose_name='コメントタイトル')
    username = models.CharField(max_length=255, verbose_name='ニックネーム')
    text = models.TextField(verbose_name='コメント本文')
    target = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
