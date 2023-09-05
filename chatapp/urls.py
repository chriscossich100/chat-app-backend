from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logintesting/', views.logintesting, name='logintesting'),
    path('createchatroom2/', views.CreateChatRoom2.as_view(), name='createchatroom2'),
    path('gettingmessages/<slug:messagesinchat>/', views.GettingMessages.as_view(), name='gettingmessages'),
    path('createmessages/<slug:chatroom>/', views.CreateMessages.as_view(), name='createmessages'),
    path('gettingchatrooms/', views.GettingChatRooms.as_view(), name='gettingchatrooms'),
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('yourchatrooms/', views.YourChatRooms.as_view(), name='yourchatrooms'),
]
