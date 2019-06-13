from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_info/<id>', views.movie_info, name='movie_info'),
    path('characters/<id>', views.characters, name='characters'),
    path('starships/<id>', views.starships, name='starships'),
    path('planets/<id>', views.planets, name='planets'),

]
