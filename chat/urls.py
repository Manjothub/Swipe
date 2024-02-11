from django.urls import path,include
from.views import *

urlpatterns = [
    path('',LOGIN,name='login'),
    path('room',CHATROOM,name='room'),
    path('register',REGISTER,name='register'),
    path('saveinfo',SAVEUSER,name='saveinfo'),
    
    
    # Auth Urls
    path('dologin',DOLOGIN,name='dologin'),
    path('doregister',DOREGISTER,name='doregister'),
    path('logout',LOGOUT,name='logout'),
]
