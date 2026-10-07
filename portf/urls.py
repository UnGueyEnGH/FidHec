from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),

    path('metas/', views.metas, name='metas'),


    path('lugares/', views.lugares, name='lugares'),

    path('colorimetria/', views.colorimetria, name='colorimetria'),

]

