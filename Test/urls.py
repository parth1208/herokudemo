from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('serch_result/',view=views.search,name='search'),
    path('Content/',view=views.content,name='content'),
<<<<<<< Updated upstream
    path('Content-page/',view=views.content_page,name='content_page'),
    path('Anime-page/',view=views.Anime_page,name='Anime_page'),
    path('Movie-page/',view=views.Movies_page,name='movie_page'),
    path('Webserie-page/',view=views.Webseries_page,name='Webserie_page'),
=======
>>>>>>> Stashed changes
    path('most/',view=views.most,name='most'),
]
