from django.shortcuts import render

# Create your views here.
def dashboardPage(request):
    context = {}
    return render(request,'dashboard.html',context)

def forumDetail(request):
    context = {}
    return render(request,'forumDetail.html',context)

def postDetail(request):
    context = {}
    return render(request,'postDetail.html',context)