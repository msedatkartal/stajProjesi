from django.db import models
from django.utils.text import slugify
from appMy.models import GameCard 

# Create your models here.

# Comment
class Comment(models.Model):
    text = models.TextField(("Yorum")) 
    date_now =models.DateTimeField(("Tarih - Saat"),auto_now_add = True)
    subject_brand=models.CharField(("Konu Başlığı"), max_length=100, null=True)
    game_cate= models.ForeignKey(GameCard, verbose_name=("Konuya bağlı Kategori İsmi"), on_delete=models.CASCADE, null=True)