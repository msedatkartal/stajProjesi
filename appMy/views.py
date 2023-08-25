from django.shortcuts import render,redirect
from .models import *
from appUser.models import *



def dashboardPage(request):
    gamecard = GameCard.objects.all()
    print(gamecard)
    gamecategory = CategoryGame.objects.all()
    comments = Comment.objects.all()
    comment10 = comments[::-1][0:10]

    games = GameCard.objects.values_list('gameName',flat=True)
    print(games)

    context = {
        'gamecard': gamecard,
        'gamecategory': gamecategory,
        'comments': comment10

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





