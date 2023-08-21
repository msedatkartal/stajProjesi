from appMy.models import *
from appUser.models import *

def get_login(request):
    profile_user = None
    if request.user.is_authenticated:
        try:
            profile_user = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass
    context = {
                'profile_user': profile_user
    }
    
    return context