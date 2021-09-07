from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('detail/<int:pk>',views.detail,name='detail'),
]
