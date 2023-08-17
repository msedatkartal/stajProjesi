from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *


def loginPage(request):
    context={}
    if request.method == "POST":
        submit = request.POST.get("submit")
        if submit == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect ("dashboardPage")
            else:
                messages.warning(request,"kullanıcı adı veya şifre yanlış")
                return redirect ("loginPage")
        
        if submit == "register":
            fname = request.POST.get("fname")
            username_register = request.POST.get("username_register")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            
            password_bool = email_bool = username_register_bool = True

            if password1 != password2:
                password_bool = False
                messages.warning(request,"Şifreler aynı değil")
            if User.objects.filter(email = email).exists():
                email = False
                messages.warning(request,"Bu email zaten kullanılmakta")
            if User.objects.filter(username = username_register).exists():
                username_register_bool = False

            if password_bool and email_bool and username_register_bool:
                user = User.objects.create_user(first_name = fname,email = email,username=username_register,password=password1)
                user.save()
                
                Profile.objects.create(user=user,loginUser=False)

                return redirect("dashboardPage")
    return render(request, 'login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect("dashboardPage")


# comment
def postDetail(request,pk):
    post = Comment.objects.filter(slug=pk)

    # if request.method == 'POST':
    #     text = request.POST.get("text")
    #     subject_brand = request.POST.get("subject")
    #     comment = Comment(text=text,subject_brand=subject_brand,slug=pk)
    #     comment.save()
    #     return redirect('/postDetail/<str:'+pk+'>')
    
    context = {
        "comments":comments,
        "comment":comment,
        
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

