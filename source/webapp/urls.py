from django.urls import path, include

from webapp.views import IndexView, FriendsView, DeleteFriends, MessengeCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_friend/<int:pk>/', FriendsView.as_view(), name='add_friend'),
    path('delete_friend/<int:pk>/', DeleteFriends.as_view(), name='delete_friends'),
    path('create_mesenge/<int:pk>/', MessengeCreateView.as_view(), name='send_mesenge')
]