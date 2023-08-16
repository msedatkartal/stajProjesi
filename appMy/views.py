from django.shortcuts import render,redirect
from .models import *
from appUser.models import Comment


def dashboardPage(request):
    gamecard = GameCard.objects.all()
    gamecategory = CategoryGame.objects.all()
    context = {
        'gamecard' : gamecard,
        'gamecategory' : gamecategory
    }
    return render(request,'dashboard.html',context)

def forumDetail(request,pk = None):
    comments=Comment.objects.all()
    games = GameCard.objects.filter(slug=pk).first()
    
    if request.method == 'POST':
        text = request.POST.get("text")
        subject_brand = request.POST.get("subject")
        comment = Comment(text=text,subject_brand=subject_brand)
        comment.save()
        return redirect('postDetail')
    
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