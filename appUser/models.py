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

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=None,blank=True,null=True)
    loginUser = models.BooleanField(("Girişli mi?"),blank=True,null=True)
    comment = models.ManyToManyField(Comment, verbose_name=("Kullanıcı Yorumları"),blank=True)
    phone = models.CharField(("Telefon Numarası"), max_length=50,blank=True,null=True)
    birthday = models.DateField(("Doğum Tarihi"), auto_now=False,default=None,null=True)

    def __str__(self):
        return self.user.username
    