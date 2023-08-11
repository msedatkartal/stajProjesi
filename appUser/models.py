from django.db import models

# Create your models here.

# Comment
class Comment(models.Model):
    # title = models.CharField(("Yorum Başlığı"), max_length=50)
    # topic = yorum yapılan postun veya konunun altinda gozukmesi icin //  sor
    # topic = models.ForeignKey(Card-orGameCard, verbose_name=_("topicin altına gonderilen yorum?"), on_delete=models.CASCADE, null=True)
    fname= models.CharField(("İsim Soyisim"),max_length=150)
    text = models.TextField(("Yorum")) 
    date_now =models.DateTimeField(("Tarih - Saat"),auto_now_add = True)
   
    
    def __str__(self):
        return self.fname