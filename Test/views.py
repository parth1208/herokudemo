from typing import Counter
from Test.models import Addmovies
from django.shortcuts import render
from . models import Addmovies, moviescounter

# Create your views here.


def login(request):
    return render(request,'login.html')

def index(request):
    obj=Addmovies.objects.all()
    return render(request,'index.html',{'obj':obj})

def detail(request,pk):
    obj= Addmovies.objects.filter(id=pk)
    objj=Addmovies.objects.get(id=pk)
    if moviescounter.objects.filter(movie_name=objj).exists():
        counter=moviescounter.objects.get(id=pk)
        moviescounter.objects.filter(movie_name=objj).update(Counter=counter.Counter + 1)
    else:
        moviescounter.objects.create(movie_name=objj,Counter=0)
    
    counter=moviescounter.objects.get(id=pk)
    return render(request,'photo-detail.html',{'obj':obj,'couter':counter})
