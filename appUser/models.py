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
    user=models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    username=models.CharField(("Kulanıcı Adı"), max_length=50)
    image= models.ImageField(("Profile Resmi"), upload_to='profile', )
    loginP=models.BooleanField(("Girişli mi?"))
    comment=models.ManyToManyField(Comment, verbose_name=("Kullanıcı Yorumları"))
    password=models.CharField(("Kullanıcı Şiresi"), max_length=50)
    phone=models.CharField(("Telefon Numarası"), max_length=50)
    birthday=models.DateField(("Dagum Tarihi"), auto_now=False, auto_now_add=False)
    register_date=models.DateField(("Kayıt Tarihi"), auto_now_add=True)
    email=models.CharField(("E-mail"), max_length=50, null=True)
    

    def __str__(self):
        return self.username