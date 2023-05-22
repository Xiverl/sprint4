from django.shortcuts import get_object_or_404, render

from django.contrib.auth.models import User


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
