from django.shortcuts import render

# Create your views here.
from . import models;

def show(request):
    blogList = models.Article.objects.all();
    return render(request,'show.html',{'blogList':blogList})

def add(request):
    models.Article.objects.create(title='111',content='222')
    blogList = models.Article.objects.all();
    return render(request,'show.html',{'blogList':blogList})