from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Category, Post

# TODO: Переписать index_page при помощи классов

# class IndexPageView(View):
#     def get(self, request):
#         categories = Category.objects.all()
#         return render(request, 'main/index.html', {'categories': categories})

class IndexPageView(ListView):
    queryset = Category.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'categories'

class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category_id=category_id)

class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'



# TODO: Регистрация, активация, логин, логаут
# TODO: HTML -  письмо
# TODO: Фильтрация, поиск, сортировка
# TODO: Пагинация
# TODO: Переиспользование шаблонов
# TODO: Проверка прав
# TODO: Избранное
# TODO: Дизайн

# TODO: Описание страниц