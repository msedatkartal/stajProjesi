from django.contrib import admin
from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ['gameName','gameImage','categoryName']
    
    
    
    

admin.site.register(GameCard, CardAdmin )
admin.site.register(CategoryGame)
