from django.shortcuts import render,redirect
from .models import *
from appUser.models import *
import datetime
from django.utils import timezone
from datetime import datetime
from django.db.models import F, Count
from django.db.models import Q




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
    type_post= Comment.objects.filter(typ_comment__name = "oyun")
    comments = type_post[::-1]
    
    last_ten_comments = {}
    for comment in comments:
        if last_ten_comments.__len__() >= 10:
            break
        if  not comment.subject_brand.id in last_ten_comments:
            last_ten_comments[comment.subject_brand.id] = comment

            
    # KONU DIŞI
    off_topic=Comment.objects.filter(typ_comment__name="Konu Dışı")
    topic=off_topic[::-1]
    print('game',off_topic)  
    
    # POPÜLER KONU
    popular_subjects = Subject.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[0:10]
    
    # MODAL TOTAL SUBJECT
    subject_total = {}
    for p in gamecard:
        subject_filter = Subject.objects.filter(game_cate =p).first()
        subject_comment = subject_filter.comment_number
        subject_total[p] = subject_comment
        
    print("buradasın bura bak :  ",subject_total)
    print("HEYYYYYYYYYYYYYYYYY   :  ",subject_filter.game_cate)
        
    
    context = {
        'gamecard': gamecard,
        'gamecategory': gamecategory,
        'comments': last_ten_comments.items(),
        'game_subject':game_subject.items(),
        'off_topic':topic,
        "popular_subjects":popular_subjects,
        'subject_total':subject_total
        
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




def Query(request):
    search_post=request.GET.get('q')
    comments = Comment.objects.all().order_by("-date_now")
    
    
    if search_post:
        posts=Comment.objects.filter(Q(subject_brand__subjectBrand__icontains=search_post) | Q(text__icontains=search_post))
        
    else:
        posts=None
        
    
    context={
        'posts':posts,
        'search_post':search_post,
        'comments':comments
    }

    return render(request, 'search.html',context)
    
