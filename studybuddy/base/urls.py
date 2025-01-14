from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
    path('login/',views.login_room,name='login'),
    path('logout/',views.logoutRoom,name='logout'),
    path('register/',views.register,name='register'),
    path('delete/<str:pk>/<str:room_pk>/',views.deleteMessage,name='delete'),
    
]
