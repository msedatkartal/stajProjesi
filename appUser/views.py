from django.shortcuts import render

def loginPage(request):
    context={}
    return render(request, 'login-register.html', context)
