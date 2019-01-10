from django.shortcuts import render
from django.http import HttpResponse
from shop import models
# Create your views here.



def index(request):
    return HttpResponse('你好，这是我第一个程序')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def home(request):
    return render(request,'home.html')

def add2(request,a,b):
    models.addPserson()
    c = int(a) + int(b)
    return HttpResponse(str(c))