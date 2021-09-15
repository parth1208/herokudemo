from typing import Counter
from Test.models import Addmovies
from django.shortcuts import render
from . models import Addmovies, Category, moviescounter, movieslink
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def login(request):
    return render(request,'login.html')

def index(request):
    obj=Addmovies.objects.all().order_by('-id')[:4]
    li=list(moviescounter.objects.all().order_by('Counter'))[-4:]
    link=reversed(li)
    return render(request,'index.html',{'obj':obj,'link':link})

def content(request):
    obj=Addmovies.objects.all()[:4]
    Anime = list(Addmovies.objects.filter(category_types='Anime'))[:4]
    Animes = random.sample(Anime, len(Anime))
    movie = list(Addmovies.objects.filter(category_types='movies'))[:4]
    movies = random.sample(movie, len(movie))
    webserie = list(Addmovies.objects.filter(category_types='webseries'))[:4]
    webseries = random.sample(webserie, len(webserie))
    con = {'obj':obj,
            'Animes':Animes,
            'movies':movies,
            'webseries':webseries
            }
    return render(request,'content.html',con)

def content_page(request):
    obj=Addmovies.objects.all().order_by('-id')
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'content_page.html',{'obj':post_list})

def Anime_page(request):
    obj=Addmovies.objects.filter(category_types='Anime').order_by('-id')
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'content_page.html',{'obj':post_list})

def Movies_page(request):
    obj=Addmovies.objects.filter(category_types='movies').order_by('-id')
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'content_page.html',{'obj':post_list})

def Webseries_page(request):
    obj=Addmovies.objects.filter(category_types='webseries').order_by('-id')
    paginator = Paginator(obj, 12)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'content_page.html',{'obj':post_list})

def detail(request,pk):
    obj= Addmovies.objects.filter(id=pk)
    objj=Addmovies.objects.get(id=pk)
    if moviescounter.objects.filter(movie_name=objj).exists():
        counter=moviescounter.objects.get(movie_name=pk)
        moviescounter.objects.filter(movie_name=objj).update(Counter=counter.Counter + 1)
    else:
        counter=moviescounter.objects.create(movie_name=objj,Counter=0)
    links=movieslink.objects.filter(moviesname=objj)
    li=moviescounter.objects.filter(movie_name__category_types=objj.category_types).order_by('Counter')
    related=[i for i in li if i != counter]
    nn=reversed(related[-4:])
    line=moviescounter.objects.all().order_by('Counter')
    rela=[j for j in line if j != counter and j not in related]
    most_view=reversed(rela[-4:])  
    return render(request,'photo-detail.html',{'obj':obj,'couter':counter,'links':links,'res':nn,'mostview':most_view})

def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        results = Addmovies.objects.filter(movies_name__contains=query_name)
        return render(request, 'search_result.html', {'obj':results})
    return render(request, 'search_result.html')

def most(request):
    link=moviescounter.objects.all().order_by('Counter')
    p = Paginator(link, 5)  
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number) 
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj,
                }
    return render(request,'most.html',context)