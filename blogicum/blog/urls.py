from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.PostListView.as_view(), name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.PostCreateView.as_view(), name='create_post'),
    path('profile/<str:name>/', views.info_profile, name='profile'),
    #path('profile/<str:username>/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),
]
