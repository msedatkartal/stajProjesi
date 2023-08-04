from django.urls import path
from .views import *
urlpatterns = [
    path('',dashboardPage, name='dashboardPage'),
    path('forumDetail',forumDetail, name='forumDetail'),
    path('postDetail',postDetail, name='postDetail'),
    
    
]