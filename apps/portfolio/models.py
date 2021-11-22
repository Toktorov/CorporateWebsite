from django.db import models

# Create your models here.
# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название", 
        help_text="Например Заголовок: Сегодня все пришли на урок"
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="news", verbose_name="Фото", 
        help_text="Загружайте только jpg и png формат изображении"
    )
    link = models.CharField(
        max_length=255, verbose_name="ссылка на проект", 
        help_text="Например: https://www.youtube.com/", 
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Портфолио'