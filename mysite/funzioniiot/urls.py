from django.urls import path
from . import views

app_name = 'funzioniiot'
urlpatterns = [
    path('', views.homeiot, name='homeiot'),
    
]