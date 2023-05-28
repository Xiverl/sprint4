from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('posts/<int:pk>/',
         views.PostDetailView.as_view(),
         name='post_detail'),
    path('create_post/',
         views.PostCreateView.as_view(),
         name='create_post'),
    path('edit/<int:pk>/',
         views.PostUpdateView.as_view(),
         name='edit_post'),
    path('delete/<int:pk>/',
         views.PostDeleteView.as_view(),
         name='delete_post'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),
    path('comment/<int:pk>', views.add_comment, name='add_comment'),
    path('posts/<int:post>/edit_comment/<int:pk>',
         views.edit_comment,
         name='edit_comment'),
    path('posts/s<int:post>/delete_comment/<int:pk>',
         views.delete_comment,
         name='delete_comment'),
    path('profile/<name>', views.info_profile, name='profile'),
    path('edit_profile/<slug:name>',
         views.edit_profile,
         name='edit_profile'),
]
