import json
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Profile


class IndexView(ListView):
    template_name = 'index.html'
    model = get_user_model()
    context_object_name = 'users'

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










