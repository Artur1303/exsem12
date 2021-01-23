from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'index.html'
    model = get_user_model()
    paginate_comments_by = 2
    paginate_comments_orphans = 0
    context_object_name = 'users'
