from django.urls import path
from .views import*

urlpatterns = [
    path('loginPage', loginPage , name='loginPage')
]