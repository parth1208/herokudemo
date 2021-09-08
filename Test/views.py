from Test.models import Addmovies
from django.shortcuts import render
from . models import Addmovies

# Create your views here.


def login(request):
    return render(request,'login.html')

def index(request):
    obj=Addmovies.objects.all()
    return render(request,'index.html',{'ob':obj})

def detail(request,pk):
    obj= Addmovies.objects.filter(id=pk)
    return render(request,'photo-detail.html',{'obj':obj})
