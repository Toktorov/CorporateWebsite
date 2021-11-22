from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="news", verbose_name="Фото")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'