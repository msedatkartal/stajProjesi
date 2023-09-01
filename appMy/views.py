from django.shortcuts import render,redirect
from .models import *
from appUser.models import *
import datetime
from django.utils import timezone
from datetime import datetime


def dashboardPage(request):
    # CAROUSEL
    gamecard = GameCard.objects.all()
    print(gamecard)
    game_subject={}
    for i in gamecard:
        game_comment=Comment.objects.filter( game_cate=i ).last()
        game_subject[i]=game_comment

    # MESAJ VE KONU
    gamecategory = CategoryGame.objects.all()
    comments = Comment.objects.all()[::-1]
    # comment10 = comments[::-1][0:10]
    
    last_ten_comments = {}
    # if Comment.objects.filter(typ_comment__name="oyun"):
    for comment in comments:
        if last_ten_comments.__len__() >= 10:
            break
        if  not comment.subject_brand.id in last_ten_comments:
            last_ten_comments[comment.subject_brand.id] = comment
            
    # KONU DIŞI
    
             
    context = {
        'gamecard': gamecard,
        'gamecategory': gamecategory,
        'comments': last_ten_comments.items(),
        'game_subject':game_subject.items(),
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





