from django.contrib import admin
from .models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=['username', 'loginP',]
    readonly_fields=['register_date']
    
admin.site.register(Comment)
admin.site.register(Profile,ProfileAdmin)
