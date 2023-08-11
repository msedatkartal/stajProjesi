from django.db import models



class CategoryGame(models.Model):
    categoryName = models.CharField(("Kategori İsmi"), max_length=50)
    
    def __str__(self):
        return self.categoryName

class GameCard(models.Model):
    gameName = models.CharField(("Oyun Adı"), max_length=50)
    gameImage = models.ImageField(("Oyun Resmi"), upload_to='game', max_length=200)
    categoryName=models.ForeignKey(CategoryGame, verbose_name=("kategori ismi"), on_delete=models.CASCADE)
    slug=models.SlugField(blank=True, null=True)

    
    def __str__(self):
        return self.gameName
    
    class Meta:
        verbose_name_plural="Oyun Kartları"
        verbose_name="Kart"


