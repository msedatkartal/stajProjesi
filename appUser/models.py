from django.db import models
from django.contrib.auth.models import User
from appMy.models import GameCard

# User Model

# Comment
class Comment(models.Model):
    text = models.TextField(("Yorum")) 
    date_now =models.DateTimeField(("Tarih - Saat"),auto_now_add = True)
    subject_brand=models.CharField(("Konu Başlığı"), max_length=100, null=True)
    game_cate= models.ForeignKey(GameCard, verbose_name=("Konuya bağlı Kategori İsmi"), on_delete=models.CASCADE, null=True)
   

    def __str__(self):
        return self.subject_brand