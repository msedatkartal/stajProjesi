from django.db import models
from django.utils.text import slugify

class ForumTyp(models.Model):
    name=models.CharField(("tip"), max_length=50)
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name.replace('ı','i'))
        super(ForumTyp,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
   

class CategoryGame(models.Model):
    categoryName = models.CharField(("Kategori İsmi"), max_length=50)
    slug = models.SlugField(blank=True,null= True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.categoryName.replace('ı','i'))
        super(CategoryGame,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.categoryName
    class Meta:
        verbose_name_plural = "Oyun Kategorileri"
        verbose_name= "Kategori"
        
class GameCard(models.Model):
    gameName = models.CharField(("Oyun Adı"), max_length=50)
    gameImage = models.ImageField(("Oyun Resmi"), upload_to='game', max_length=200)
    categoryName=models.ForeignKey(CategoryGame, verbose_name=("kategori ismi"), on_delete=models.CASCADE)
    slug=models.SlugField(blank=True, null=True)
    forumTyp=models.ForeignKey(ForumTyp, verbose_name=("forum tipi"), on_delete=models.CASCADE, blank=True,null=True)
   
    
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.gameName.replace('ı','i'))
        super(GameCard,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.gameName
    
    class Meta:
        verbose_name_plural="Oyun Kartları"
        verbose_name="Kart"

