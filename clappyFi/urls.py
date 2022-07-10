from django.urls import path

from clappyFi.views import home,Login,UserPage

urlpatterns = [
    path('login/',Login,name='login'),
    path('',home,name='home'),
    path('user/',UserPage, name='userpage')


]