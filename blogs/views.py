from django.views.generic import ListView, DetailView

from .models import Post, Category, Tag


class BaseListView(ListView):
    """記事の一覧表示の基底クラス"""
    paginate_by = 10

    def get_queryset(self):
        """作成日順の記事を返す."""
        # post.categoryや、post.tag.allをテンプレートで書く場合は
        # それぞれselect_relatedやprefetch_relatedで改善できる場合があります。

        queryset = Post.objects.filter(status__name='published').order_by('-created_at')\
            .prefetch_related('category', 'tag').select_related('user', 'status')
        # queryset = Post.objects.order_by('-created_at') \
        #     .prefetch_related('category', 'tag').select_related('user', 'status')
        return queryset


class PostIndexView(BaseListView):
    """トップページ"""
    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context['category_list'] = self.get_queryset()
    #     return context


class CategoryView(BaseListView):
    """カテゴリで絞込む"""
    def get_queryset(self):
        category_id = self.kwargs['pk']
        self.category = Category.objects.get(id=category_id)
        queryset = super().get_queryset().filter(category=self.category)
        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        """クリックされたカテゴリを保持"""
        context = super().get_context_data(*args, **kwargs)
        context['category'] = self.category
        return context


class TagView(BaseListView):
    """タグで絞り込む"""
    def get_queryset(self):
        tag_id = self.kwargs['pk']
        self.tag = Tag.objects.get(id=tag_id)
        queryset = super().get_queryset().filter(tag=self.tag)
        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        """クリックされたタグを保持"""
        context = super().get_context_data(*args, **kwargs)
        context['tag'] = self.tag
        return context


class PostDetail(DetailView):
    model = Post


class CategoryListView(ListView):
    model = Category


class TagListView(ListView):
    model = Tag


# class CategoryPostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(category__pk=self.kwargs['pk'])
#         return queryset
