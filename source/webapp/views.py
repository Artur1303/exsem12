from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, CreateView
from rest_framework.generics import get_object_or_404
from accounts.models import Profile
from webapp.forms import MessangeForm
from webapp.models import Message


class IndexView(ListView):
    template_name = 'index.html'
    model = get_user_model()
    context_object_name = 'users'
    paginate_by = 2
    paginate_orphans = 0

    def get_queryset(self):
        my_user = super().get_queryset().exclude(pk=self.request.user.pk)
        return my_user


class FriendsView(View):

    def post(self, request, *args, **kwargs):
        friend = get_object_or_404(Profile, pk=self.kwargs.get('pk'))
        profile = self.request.user.profile
        profile.friends.add(friend)
        return HttpResponse({"message": "Добавленно"})


class DeleteFriends(View):
    def delete(self, request, *args, **kwargs):
        friend = get_object_or_404(Profile, pk=self.kwargs.get('pk'))
        profile = self.request.user.profile
        print(profile)
        profile.friends.remove(friend)
        return HttpResponse({"message": "Удален"})


class MessengeCreateView(CreateView):
    template_name = 'create_messenge.html'
    form_class = MessangeForm
    model = Message

    def form_valid(self, form):
        user = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        message = form.save(commit=False)
        message.from_whom = self.request.user
        message.to_whom = user
        if message.to_whom == self.request.user:
            return messages.error(self.request, 'Вы пытаетесь отправить сообщения самому самому')

        message.save()
        return redirect('webapp:index')








