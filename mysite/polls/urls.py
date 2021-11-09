from django.urls import path

from . import views

urlpatterns = [
    path('pollstext', views.index, name='indextext'),
    path('polls', views.index, name='index'),
]
