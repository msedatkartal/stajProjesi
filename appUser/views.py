from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *
from appMy.models import *
from django.http import HttpResponse



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
                
                image = Profileimage(image='profile/owl.png')
                image.save()
                Profile.objects.create(user=user,loginUser=False,image=image)

                return redirect("dashboardPage")
    return render(request, 'login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect("dashboardPage")


# comment
def postDetail(request, category, pk):
    games = GameCard.objects.filter(slug=category).first()
    print(category)
    subject = Subject.objects.filter(slug=pk).first()
    print(subject)
    comments = Comment.objects.filter(subject_brand__subjectBrand =subject)
    subject_author = comments.first()
    
 
    if request.user.is_authenticated:
        user = Profile.objects.filter(user = request.user).first()
    else:
        user = Profile.objects.all()
        
    if request.method == 'POST':
        
        text = request.POST.get("text")
        comment = Comment(text=text,subject_brand=subject,author=request.user, image= user.image)
        comment.save()
        return redirect('/blog/'+category+'/'+ pk )
    
    context = {
        "comments":comments,
        "subject":subject,
        "games":games,
        'subject_author':subject_author,
        }
    
    return render(request,'postDetail.html',context)
    

def messagePost(request, game_slug):
    # game_slug a göre messagepostu getirme
    try:
        game = GameCard.objects.get(slug=game_slug) 
        user = Profile.objects.filter(user = request.user).first() 

        
    except GameCard.DoesNotExist:
        return HttpResponse("Oyun bulunamadı.")
    
    # game_slug a göre konu başlığı oluşturup yorumu kaydetme
    if request.method == 'POST':
        subject_slug = request.POST.get("subject")  
        print(subject_slug)
        text = request.POST.get("text")
        subject_title=Subject(subjectBrand=subject_slug,game_cate=game)
        subject_title.save()
        subject_url = Subject.objects.filter().last()
        
        print("son konu:", subject_url)
      
        comment = Comment(text=text, subject_brand=subject_title, author=request.user, game_cate=game,image= user.image)
        comment.save()
        return redirect('/blog/'+game_slug+'/'+str((subject_url.slug)))    
    context = {
        'game': game,
    }
    return render(request, 'messagePost.html', context)




def accountUser(request):
    profile = Profile.objects.filter(loginUser=True, user=request.user).first()
    user = User.objects.filter(username=request.user).first()
    
    if request.method == "POST":
        submit = request.POST.get("submit")
        
        # Profil fotografı güncelleme
        if submit == "profileChange":
            profile_list = Profile.objects.filter(user=request.user)

            image2 = request.FILES.get("image2")
            pid = request.POST.get("id")
            
            profile2 = profile_list.get(id=pid)

            if image2 is not None:
                # User profiline ait resim
                profile_image = Profileimage(image=image2)
                profile_image.save()
                profile2.image = profile_image  # Bu kısmı eklemeyi unutmayın
                profile2.save()

        # Hesap iptali
        if submit == "subscribeUnfollow":
            user = request.user
            user.delete()
            messages.warning(request,"Hesabınız iptal edilmiştir!!")
            return redirect("dashboardPage")
            
        # Şifre güncelleme
        elif submit == "passwordUpdate":
            password = request.POST.get("password")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            
            if user.check_password(password) and password1 == password2:
                user.profile.password = password1
                user.profile.save()
                
                user.set_password(password1)
                user.save()
                return redirect("loginPage")
            else:
                messages.warning(request, "Şifreniz yanlış veya yeni şifreler aynı değil!!")
        
        #  Tel güncelleme
        elif submit == "telUpdate":
            phone = request.POST.get("tel")
            password = request.POST.get("password")
            
            if user.check_password(password):
                user.profile.phone = phone
                user.profile.save()
            else:
                messages.warning(request,"Şifre yanlış!!")
                
        # E mail güncelleme
        elif submit == "emailUpdate":
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            email_bool = True
            if User.objects.filter(email=email).exists():
               email_bool = False
               messages.warning(request, "Girdiğiniz email başkası tarafından kullanılıyor!")
            
            if user.check_password(password):
                if email_bool:
                    user.email = email
                    user.save()
            else:
                messages.warning(request, "Şifreniz yanlış!")
        
        return redirect("accountUser")
    
    context = {
        'profile': profile
    }
    
    return render(request,'accountUser.html', context)
