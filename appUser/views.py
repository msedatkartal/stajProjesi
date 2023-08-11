from django.shortcuts import render,redirect
from .models import *
def loginPage(request):
    context={}
    return render(request, 'login-register.html', context)



# comment
def postDetail(request):
    comments = Comment.objects.all()
    # comments = Comment.objects.filter(topic-or-post = topic-or-post)
    
    if request.method == 'POST':
        fname = request.POST.get("fname")
        text = request.POST.get("text")
        
        print("gelen data", fname, text)
        
        comment = Comment(fname=fname, text=text)
        comment.save()
        return redirect('postDetail')
        
    else:
   
        print("get istegi")
        context = {
            "comments":comments,
        }
        return render(request,'postDetail.html',context)