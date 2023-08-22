from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','loginUser','id']
    readonly_fields = ['loginUser']

class CommentAdmin(admin.ModelAdmin):
    list_display= ['subject_brand','game_cate','author','date_now']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Subject)