from django.shortcuts import render,redirect
from .models import *
def loginPage(request):
    context={}
    return render(request, 'login-register.html', context)

# comment
def postDetail(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        text = request.POST.get("text")
        subject_brand = request.POST.get("subject")
        comment = Comment(text=text,subject_brand=subject_brand)
        comment.save()
        return redirect('postDetail')
    
    context = {
        "comments":comments,
        }
    
    return render(request,'postDetail.html',context)
    
    
    
    
def messagePost(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        print("asd")
        subject_brand = request.POST.get("subject")
        text = request.POST.get("text")
        comment = Comment(text=text, subject_brand=subject_brand)
        comment.save()
        return redirect('forumDetail')
    print("comment", comments )
    context={
        "comments":comments,
    }
    return render (request, 'messagePost.html', context)