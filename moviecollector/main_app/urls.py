from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='movies_index'),
    path('movies/<int:movie_id>/', views.movies_show, name='movies_show')
]