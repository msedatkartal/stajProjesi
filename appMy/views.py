from django.shortcuts import render,redirect
from .models import *
from appUser.models import *
import datetime
from django.utils import timezone
from datetime import datetime



def dashboardPage(request):
    gamecard = GameCard.objects.all()
    gamecategory = CategoryGame.objects.all()
    comments = Comment.objects.all()
    comment10 = comments[::-1][0:10]
    birthday= Profile.objects.filter(birthday__day=datetime.now().date().day, birthday__month=datetime.now().date().month)

    context = {
        'gamecard': gamecard,
        'gamecategory': gamecategory,
        'comments': comment10,
        'birthday_watch': birthday,
    }
    return render(request, 'dashboard.html', context)

def forumDetail(request,pk = None):
    comments=Comment.objects.filter(game_cate__slug=pk)
    games = GameCard.objects.filter(slug=pk).first()
    subject = Subject.objects.filter(game_cate__slug=pk)
    if request.user.is_authenticated:
        user = Profile.objects.filter(user = request.user).first()
    else:
        user = Profile.objects.all()
    
    print(subject)
   
    
    if pk == None:
        pk = GameCard.objects.all()
    else:
        pk = GameCard.objects.get(slug=pk)
    context = {
        'comments':comments,
        'pk':pk,
        'games':games,
        'subject':subject
    }
    return render(request,'forumDetail.html',context)





def accountUser(request):
    context = {}
    return render(request,'accountUser.html',context)