from django.db import models

class Service(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например: Web development"
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="service", verbose_name="Фото", 
        help_text="Загружайте только jpg и png формат изображении"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Услуги'