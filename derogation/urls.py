from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('login', views.logIn, name='login'),
    path('suivi', views.suivi, name='suivi')
]