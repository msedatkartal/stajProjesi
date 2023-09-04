from appMy.models import *
from appUser.models import *
from datetime import datetime


def get_login(request):
    user_active = Profile.objects.filter(loginUser=True)
    
    bool_num = 0
    for i in user_active:
        bool_num += 1
        
    subject_number = Subject.objects.all()
    subject_num = 0
    for subject in subject_number:
        subject_num += 1
    
    comment_number = Comment.objects.all()
    comment_num = 0
    for comment in comment_number:
        comment_num += 1
    
    profile_number = Profile.objects.all()
    profile_num = 0
    for name in profile_number:
        profile_num += 1
    
    user_last = Profile.objects.filter().last()
    
    comments = Comment.objects.all()
    comment3 = comments[::-1][0:3]
    profile_user = None
    if request.user.is_authenticated:
        try:
            profile_user = Profile.objects.filter(user=request.user,loginUser = True).first()
        except Profile.DoesNotExist:
            pass
    birthday= Profile.objects.filter(birthday__day=datetime.now().date().day, birthday__month=datetime.now().date().month)
    
    
    context = {
                'profile_user': profile_user,
                'birthday_watch': birthday,
                'user_active':user_active,
                'bool_num': bool_num,
                'comment3':comment3,
                'subject_num':subject_num,
                'comment_num':comment_num,
                'profile_num':profile_num,
                'user_last':user_last
    }
    
    return context