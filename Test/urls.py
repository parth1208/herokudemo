from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('serch_result/',view=views.search,name='search'),
    path('Content/',view=views.content,name='content'),
    path('most/',view=views.most,name='most'),
]
