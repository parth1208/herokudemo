from typing import Counter
from Test.models import Addmovies
from django.shortcuts import render
from . models import Addmovies, moviescounter, movieslink

# Create your views here.


def login(request):
    return render(request,'login.html')

def index(request):
    obj=Addmovies.objects.all().order_by('-id')[:4]
    link=moviescounter.objects.all().order_by('Counter')[:4]
    return render(request,'index.html',{'obj':obj,'link':link})

def content(request):
    obj=Addmovies.objects.all()
    return render(request,'content.html',{'obj':obj})

def detail(request,pk):
    obj= Addmovies.objects.filter(id=pk)
    objj=Addmovies.objects.get(id=pk)
    if moviescounter.objects.filter(movie_name=objj).exists():
        counter=moviescounter.objects.get(id=pk)
        moviescounter.objects.filter(movie_name=objj).update(Counter=counter.Counter + 1)
    else:
        moviescounter.objects.create(movie_name=objj,Counter=0)
    counter=moviescounter.objects.get(id=pk)
    links=movieslink.objects.filter(moviesname=objj)
    return render(request,'photo-detail.html',{'obj':obj,'couter':counter,'links':links})

def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name == "null":
            return render(request, 'index.html')
        else:
            results = Addmovies.objects.filter(movies_name__contains=query_name)
            return render(request, 'search_result.html', {'obj':results})
    return render(request, 'search_result.html')

def most(request):
    link=moviescounter.objects.all().order_by('Counter')
    return render(request,'most.html',{'link':link})