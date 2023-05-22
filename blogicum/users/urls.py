from users import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('profile/<name>', views.info_profile,  name='login'),
]
