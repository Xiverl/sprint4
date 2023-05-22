from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
import datetime as dt

from blog.models import Post, Category
from django.contrib.auth.models import User
from blog.forms import PostForm
from blogicum.settings import MAX_POST


def index(request):
    template = 'blog/index.html'
    current_time = dt.datetime.now()
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True
    )[:MAX_POST]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    current_time = dt.datetime.now()
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=current_time,
            category__is_published=True
        ),
        pk=id
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    templates = 'blog/category.html'
    current_time = dt.datetime.now()
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = category.posts.filter(
        pub_date__lte=current_time,
        is_published=True,
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, templates, context)


def my_profile(request, username):
    templates = 'blog/profile.html'
    return render(request, templates)


def info_profile(request, name):
    templates = 'blog/profile.html'
    user = get_object_or_404(
        User,
        username=name,
    )
    profile_post = user.posts.all()
    context = {
        'page_obj': profile_post,
    }
    return render(request, templates, context)


class PostListView(ListView):
    template_name = 'blog/index.html'
    current_time = dt.datetime.now()
    model = Post
    queryset = Post.objects.filter(
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True
    ).select_related('author')
    ordering = '-pub_date'
    paginate_by = 10


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    def form_valid(self, form):
        # Присвоить полю author объект пользователя из запроса.
        form.instance.author = self.request.user
        # Продолжить валидацию, описанную в форме.
        return super().form_valid(form)
