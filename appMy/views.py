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

def forumDetail(request):
    comments=Comment.objects.all()
    
    if request.method == 'POST':
        text = request.POST.get("text")
        subject_brand = request.POST.get("subject")
        comment = Comment(text=text,subject_brand=subject_brand)
        comment.save()
        return redirect('postDetail')
    context = {
        'comments':comments,
        
        
    }
    return render(request,'forumDetail.html',context)





