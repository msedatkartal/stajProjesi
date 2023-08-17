from django.db import models
from django.contrib.auth.models import User
from appMy.models import GameCard
from django.utils.text import slugify

# User Model
class Subject(models.Model):
    subjectBrand = models.CharField(("Konu Başlığı"), max_length=50)
    slug = models.SlugField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        if self.subjectBrand:
            self.slug = slugify(self.subjectBrand.replace("ı", "i"))
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return self.subjectBrand
# Comment
class Comment(models.Model):
    text = models.TextField(("Yorum")) 
    date_now =models.DateTimeField(("Tarih - Saat"),auto_now_add = True)
    subject_brand=models.ForeignKey(Subject, verbose_name=("Konu Başlığı"), on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(User, verbose_name=("Yazar"), on_delete=models.CASCADE, null=True)
    game_cate= models.ForeignKey(GameCard, verbose_name=("Konuya bağlı Kategori İsmi"), on_delete=models.CASCADE, null=True)    

   

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=None,blank=True,null=True)
    loginUser = models.BooleanField(("Girişli mi?"),blank=True,null=True)
    comment = models.ManyToManyField(Comment, verbose_name=("Kullanıcı Yorumları"),blank=True)
    phone = models.CharField(("Telefon Numarası"), max_length=50,blank=True,null=True)
    birthday = models.DateField(("Doğum Tarihi"), auto_now=False,default=None,null=True)

    def __str__(self):
        return self.user.username
    