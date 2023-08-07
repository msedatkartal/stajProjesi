from django.shortcuts import render
from .models import *


def dashboardPage(request):
    gamecard = GameCard.objects.all()
    gamecategory = CategoryGame.objects.all()
    context = {
        'gamecard' : gamecard,
        'gamecategory' : gamecategory
    }
    return render(request,'dashboard.html',context)

def forumDetail(request):
    context = {}
    return render(request,'forumDetail.html',context)

def postDetail(request):
    context = {}
    return render(request,'postDetail.html',context)