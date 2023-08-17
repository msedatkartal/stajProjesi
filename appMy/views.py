from django.shortcuts import render,redirect
from .models import *
from appUser.models import *


def dashboardPage(request):
    gamecard = GameCard.objects.all()
    gamecategory = CategoryGame.objects.all()
    
    profile_user = None
    if request.user.is_authenticated:
        try:
            profile_user = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass
    
    context = {
        'gamecard': gamecard,
        'gamecategory': gamecategory,
        'profile_user': profile_user
    }
    return render(request, 'dashboard.html', context)

def forumDetail(request,pk = None):
    comments=Comment.objects.filter(game_cate__slug=pk)
    games = GameCard.objects.filter(slug=pk).first()
    
    if pk == None:
        pk = GameCard.objects.all()
    else:
        pk = GameCard.objects.get(slug=pk)
    context = {
        'comments':comments,
        'pk':pk,
        'games':games
        
    }
    return render(request,'forumDetail.html',context)





def accountUser(request):
    context = {}
    return render(request,'accountUser.html',context)