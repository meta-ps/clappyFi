from django.urls import path

from clappyFi.views import home,Login,UserPage,Refer

urlpatterns = [
    path('login/',Login,name='login'),
    path('',home,name='home'),
    path('user/',UserPage, name='userpage'),
    path('user/refer/<str:zzz>/',Refer,name='Refer')


]