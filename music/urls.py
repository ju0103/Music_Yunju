from django.urls import path

from music import views

urlpatterns = [
    path('', views.list_musics, name = 'list_musics'),
    path('new/', views.create_music, name='add_music'),
    path('update/<int:id>/', views.update_music, name = 'update_music'),
    path('delete/<int:id>/', views.delete_music, name = 'delete_music'),
    path('search_basic/', views.search_basic, name = 'search_music'),
]
